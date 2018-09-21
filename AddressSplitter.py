import re
class Solution(object):
    def string_to_json(self,address):
        ad = address.split()
        l=len(ad)

        data_d = []
        integer_indexes=[]
        for a in ad:
            data={'integer':False,'data':a}
            if re.findall('[0-9]+', a):
                data['integer']=True
                data_d.append(data)
                integer_indexes.append(ad.index(a))

        #If there is only one integer
        if len(integer_indexes) == 1:
            index = integer_indexes[0]
            print index
            if index == l-1:
                street= ' '.join(ad[0:l-1])
                hnumber = ad[l-1].strip(',')
                j = {'street':street,'housenumber':hnumber}
                print j
                return j
            elif index == 0:
                street = ' '.join(ad[1:l])
                hnumber = ad[0].strip(',')
                j = {'street': street, 'housenumber': hnumber}
                print j
                return j
            else:
                street = ' '.join(ad[0:index])
                hnumber = ' '.join(ad[index:l]).strip(',')
                j = {'street': street, 'housenumber': hnumber}
                print j
                return j
        if len(integer_indexes) == 2:
            index1 = integer_indexes[0]
            index2 = integer_indexes[1]
            street = ' '.join(ad[0:index1+1])
            hnumber = ' '.join(ad[index1+1:l])
            j = {'street': street, 'housenumber': hnumber}
            print j
            return j


    def addess_separator(self,addresses):
        pass
        str_add = []
        for ad in addresses:
            str_add.append(self.string_to_json(ad))


s=Solution()
#s.string_to_json('Calle 39 No 1540')
s.string_to_json('4, rue de la revolution')
#s.string_to_json('Calle Aduana, 29')
#s.string_to_json('Auf der Vogelwiese 23 b')
#s.string_to_json('Blaufeldweg 123B')
s.string_to_json('12 Blaufeldweg  54B')