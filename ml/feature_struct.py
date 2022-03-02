# -*- coding:utf-8 -*-


from  pystruct import Struct

#class _feature_struct():
#    def __init__(self,self,creator,def_val = 0.0):

_feature_info_manager = {}
class FeatureStruct(Struct):
    def __init__(self,creator,def_val = 0.0,array = None):
        self.__lenth__ = creator.lenth
        self.__feature_infos__ =creator.feature_infos
        self.__feature_names__ = creator.feature_names
        if array:
            assert len(array) == self.__lenth__,(len(array),self.__lenth__)
            for feature_name in self.__feature_names__:
                info = self.__feature_infos__[feature_name]
                if info.lenth ==1:
                    self[info.name] = array[info.offset]
                else:
                    self[info.name] = array[info.offset:info.offset+info.lenth]
        else:
            for feature_name in self.__feature_names__:
                info = self.__feature_infos__[feature_name]
                if info.lenth ==1:
                    self[info.name] = def_val
                else:
                    self[info.name] = [def_val]*info.lenth


    def update(self,other):
        for feature_name in other.__feature_names__:
            self[feature_name] = other[feature_name]

    def __setitem__(self, key, value):
        assert '__' in key or key in self.__feature_names__ ,key
        if '__' not in  key  and self.__feature_infos__[key].lenth != 1:
            assert len(value)==self.__feature_infos__[key].lenth  ,(len(value),self.__feature_infos__[key].lenth)
        Struct.__setitem__(self,key,value)

    def __getitem__(self, item):
        assert '__' in item or item in self.__feature_names__,item
        return Struct.__getitem__(self,item)

    def toarray(self):
        arr = []
        for feature_name in self.__feature_names__:
            info = self.__feature_infos__[feature_name]
            if info.lenth == 1:
                arr.append(self[info.name])
            else:
                arr.extend(self[info.name])
        assert len(arr) ==self.__lenth__,(len(arr),self.__lenth__)

        return arr








class FeatureStructCreator():
    def __init__(self,config):
        self.lenth = 0
        self.feature_infos = {}
        self.feature_names = []
        for feature_name,lenth in config:
            sf = Struct(name = feature_name,lenth = lenth,offset = self.lenth)
            self.lenth+=lenth
            self.feature_infos[feature_name] = sf
            assert feature_name not in self.feature_names,feature_name
            self.feature_names.append(feature_name)

    def print_index(self):
        for feature_name in self.feature_names:
            length = self.feature_infos[feature_name].lenth
            offset = self.feature_infos[feature_name].offset
            if length>1:

                print(feature_name,str(offset)+'-'+str(offset+length-1))
            else:
                print( feature_name,offset)

    def feature_name_by_index(self):
        names = []
        for feature_name in self.feature_names:
            length = self.feature_infos[feature_name].lenth
            if length>1:
                for i in range(length):
                    names.append(feature_name+'_'+str(i))
            else:
                names.append(feature_name)
        return names

    def zeros(self):
        return FeatureStruct(self)

    def ones(self):
        return FeatureStruct(self,def_val=1.0)

    def from_array(self,array):
        return FeatureStruct(self, array=array)

    def loads(self,s):
        arr =[float(i) for i in s.split(' ')]
        return self.from_array(arr)

if __name__ == '__main__':
    conf = [('F',2),
            ('D', 3),
            ('C', 1),
            ]

    fsc = FeatureStructCreator(conf)
    feature = fsc.from_array([1,2,3,4,5,6])
    print(feature.F,feature.D,feature.C)
    print(feature.toarray())





