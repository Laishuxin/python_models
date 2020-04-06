import numpy as np
import pandas as pd
import plotly.express as px


class Topsis(object):
    """
    利用pandas实现优劣解析法
    """

    def __init__(self):
        """
        初始化

        Parameters
        ----------
        file : str
            excel表格文件
        """
        # self.inputMatrix = self.__read_data(file)
        # self._weightVec = None
        pass

    def __read_data(self, file):
        return pd.read_excel(file, index_col=0)

    def __map_func(self, t):
        ret = 1
        if (t == "negative"):
            ret = 2
        elif (t == "middle"):
            ret = 3
        elif (t == "interval"):
            ret = 4
        return ret

    def __interval_to_max(self, x, lower, upper, M):
        if (x < lower):
            return 1 - (lower - x) / M
        elif (x > upper):
            return 1 - (x - upper) / M
        else:
            return 1

    def normalize(self, matrix):
        """
        归一化

        Parameters
        ----------
        matrix : pd.Dataframe
            需要归一化的矩阵, 向量

        Returns
        -------
            归一化后的矩阵
        """
        return matrix / matrix.sum(axis=0)

    def positive(self, matrix, types=None, argsDic=None):
        """
        正向化输入矩阵

        Parameters
        ----------
        matrix : pd.Dataframe
            待正向化的矩阵
        types : list
            指标类型列表
            {"positive" : 1，  # 极大型
             "negative" : 2,   # 极小型
             "middle"   : 3,   # 中间型
             "interval" : 4,   # 区间型
            }
        argsDic : dict
            中间型和区间型参数字典.
            key   : 第i个指标
            value : 中间型输入中间值,区间型输入区间元组
        """
        # 如果没有输入类型，默认不正向化
        if types is None:
            return matrix

        positivedMatrix = matrix.copy()
        # 将str类型映射为int类型，极大型不做处理
        types_map = list(map(self.__map_func, types))
        for i in range(len(types_map)):
            tempCol = matrix.iloc[:, i]
            # 极小型
            if (types_map[i] == 2):
                max_ = np.max(tempCol)
                positivedMatrix.iloc[:, i] = max_ - tempCol
            # 中间型
            elif (types_map[i] == 3):
                middle = argsDic.get(i)
                if (middle is None):
                    raise ValueError("第{}个指标为中间型，请在字典中传入中间值".format(i))
                M = np.max(np.abs(tempCol - middle))
                positivedMatrix.iloc[:, i] = 1 - (np.abs(tempCol - middle) / M)
            # 区间型
            elif (types_map[i] == 4):
                interval = argsDic.get(i)
                if (interval is None):
                    raise ValueError("第{}个指标为区间型，请在字典中传入区间".format(i))
                M = max(interval[0] - np.min(tempCol),
                        np.max(tempCol) - interval[1])
                positivedMatrix.iloc[:, i] = tempCol.apply(
                    self.__interval_to_max, args=(interval[0], interval[1], M))
        return positivedMatrix

    def standardize(self, matrix):
        """
        标准化

        Parameters
        ----------
        matrix : pd.Dataframe
            正向化后的矩阵

        Returns
        -------
        标准化后的矩阵
        """
        squareSum = (self.inputMatrix * self.inputMatrix).sum(axis=0)
        return matrix / np.sqrt(squareSum)

    def compute_good_and_bad(self, standardizedMatrix):
        """
        求出优劣解

        Parameters
        ----------
        standardizedMatrix : pd.DataFrame
            以标准化的正向指标矩阵

        Returns
        -------
        goodVec : pd.Series
            优解向量
        badVec : pd.Series
            劣解向量
        """
        goodVec = standardizedMatrix.max()
        badVec = standardizedMatrix.min()
        return goodVec, badVec

    def get_score(self, standardizedMatrix, goodVec, badVec, weightVec=None, ascending=False):
        """
        计算每个评价对象的得分
        Parameters
        ----------
        standardizedMatrix : pd.DataFrame
            以标准化的正向指标矩阵
        goodVec : pd.Series
            优解向量
        badVec : pd.Series
            劣解向量
        weightVec : pd.Series
            权重向量
            
        Returns
        -------
        scores : pd.Series
            每个评价对象的的得分，默认按升序排序
        """
        if (weightVec is None):
            dGoodVec = ((standardizedMatrix - goodVec)**2).sum(axis=1)
        else:
            dGoodVec = ((standardizedMatrix - goodVec)**2 * weightVec).sum(axis=1)
        dBadVec = ((standardizedMatrix - badVec)**2 * weightVec).sum(axis=1)
        scores = dBadVec / (dGoodVec + dBadVec)
        return scores.sort_values(ascending=False)
        
    def load_data(self, file, weightVec=None):
        """
        获取数据

        Parameters
        ----------
        file : str
            excel表格文件
        """
        self.inputMatrix = self.__read_data(file)
        # 如果输入权重向量，则先将权重向量归一化
        self._weightVec = weightVec
        if (weightVec is not None):
            self._weightVec = self.normalize(weightVec)

    def transform(self, types=None, argsDic=None, ascending=False):
        """
        计算每个评价对象的等分, 默认按降序排序
        Parameters
        ----------
        types : list
            指标类型列表
            {"positive" : 1，  # 极大型
             "negative" : 2,   # 极小型
             "middle"   : 3,   # 中间型
             "interval" : 4,   # 区间型
            }
        argsDic : dict
            中间型和区间型参数字典.
            key   : 第i个指标
            value : 中间型输入中间值,区间型输入区间元组
        ascending : bool
            是否升序排序
        
        Returns
        -------
        scores : pd.Series
            每个评价对象排序后的得分
        """
        # 1.正向化
        self._positivedMatrix = self.positive(self.inputMatrix, types, argsDic)
        # 2.标准化
        self._standardizedMatrix = self.standardize(self._positivedMatrix)
        # 3.求出优劣解
        self._goodVec, self._badVec = self.compute_good_and_bad(
            self._standardizedMatrix)
        # 4.计算加权得分，并排序
        self.scores = self.get_score(
            self._standardizedMatrix, self._goodVec, self._badVec, self._weightVec, ascending)
        return self.scores

    def fit_transform(self):
        pass


if __name__ == '__main__':
    topsis = Topsis()
    topsis.load_data("data/20条河流的水质情况数据.xlsx")
    topsis.transform(types=['positive', 'middle', 'negative', 'interval'], argsDic={1:7, 3:(10, 20)})