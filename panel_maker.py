import itertools
import pandas as pd


class set_panel(object):

    def __init__(self, panel, start_year, end_year):
        iso = ['AFG','ALB','DZA','AND','AGO','ATG','ARG','ARM','AUS','AUT',
                'AZE','BHS','BHR','BGD','BRB','BLR','BEL','BLZ','BEN','BTN',
                'BOL','BIH','BWA','BRA','BRN','BGR','BFA','BDI','CPV','KHM',
                'CMR','CAN','CYM','CAF','TCD','CHL','CHN','COL','COG','CRI',
                'CIV','HRV','CUB','CYP','CZE','PRK','COD','DNK','DJI','DOM',
                'ECU','EGY','SLV','GNQ','ERI','EST','ETH','FRO','FLK','FJI',
                'FIN','FRA','GAB','GMB','GEO','DEU','GHA','GIB','GRC','GRD',
                'GLP','GTM','GIN','GNB','GUY','HTI','HND','HUN','ISL','IND',
                'IDN','IRN','IRQ','IRL','ISR','ITA','JAM','JPN','JOR','KAZ',
                'KEN','KIR','KWT','KGZ','LAO','LVA','LBN','LSO','LBR','LBY',
                'LIE','LTU','LUX','MDG','MWI','MYS','MDV','MLI','MLT','MHL',
                'MTQ','MRT','MUS','MEX','FSM','MCO','MNG','MNE','MAR','MOZ',
                'MMR','NAM','NRU','NPL','NLD','NZL','NIC','NER','NGA','NOR',
                'OMN','PAK','PLW','PAN','PNG','PRY','PER','PHL','POL','PRT',
                'PRI','QAT','KOR','MDA','ROU','RUS','RWA','KNA','LCA','VCT',
                'WSM','SMR','STP','SAU','SEN','SRB','SYC','SLE','SGP','SVK',
                'SVN','SLB','SOM','ZAF','SSD','ESP','LKA','PSE','SDN','SUR',
                'SJM','SWZ','SWE','CHE','SYR','TJK','THA','MKD','TLS','TGO',
                'TON','TTO','TUN','TUR','TKM','TCA','TUV','UGA','UKR','ARE',
                'GBR','TZA','USA','VIR','URY','UZB','VUT','VEN','VNM','YEM',
                'ZMB','ZWE']
        if panel=='ISO':
            self.panel = iso
        else:
            self.panel = panel
        self.start_year = start_year
        self.end_year = end_year

    def monadic_month(self):
        list_holder = []
        for year in xrange(self.start_year, self.end_year+1):
            for actor in self.panel:
                for month in xrange(1,13):
                    dict_holder = {'Actor':actor, 'Year':year, 'Month':month}
                    list_holder.append(dict_holder)
        return list_holder

    def monadic_year(self):
        list_holder = []
        for year in xrange(self.start_year, self.end_year+1):
            for actor in self.panel:
                dict_holder = {'Actor':actor, 'Year':year}
                list_holder.append(dict_holder)
        return list_holder

    def directed_dyad_month(self):
        list_holder = []
        dyad_list = list(itertools.permutations(self.panel,2))
        for year in xrange(self.start_year, self.end_year+1):
            for dyad in dyad_list:
                for month in xrange(1,13):
                    dict_holder = {'Actor 1':dyad[0], 'Actor 2':dyad[1], 
                            'Year':year, 'Month':month}
                    list_holder.append(dict_holder)
        return list_holder

    def undirected_dyad_month(self):
        list_holder = []
        dyad_list = list(itertools.combinations(self.panel,2))
        for year in xrange(self.start_year, self.end_year+1):
            for dyad in dyad_list:
                for month in xrange(1,13):
                    dict_holder = {'Actor 1':dyad[0], 'Actor 2':dyad[1], 
                            'Year':year, 'Month':month}
                    list_holder.append(dict_holder)
        return list_holder

    def directed_dyad_year(self):
        list_holder = []
        dyad_list = list(itertools.permutations(self.panel,2))
        for year in xrange(self.start_year, self.end_year+1):
            for dyad in dyad_list:
                dict_holder = {'Actor 1':dyad[0], 'Actor 2':dyad[1],
                        'Year':year}
                list_holder.append(dict_holder)
        return list_holder

    def undirected_dyad_year(self):
        list_holder = []
        dyad_list = list(itertools.combinations(self.panel,2))
        for year in xrange(self.start_year, self.end_year+1):
            for dyad in dyad_list:
                dict_holder = {'Actor 1':dyad[0], 'Actor 2':dyad[1],
                        'Year':year}
                list_holder.append(dict_holder)
        return list_holder

    def create_panel(self, filename, layout='monadic', level='year'):
        if layout=='monadic':
            if level=='year':
                df=pd.DataFrame(self.monadic_year())
                df.to_csv(filename, index=False)
            elif level=='month':
                df=pd.DataFrame(self.monadic_month())
                df.to_csv(filename, index=False)
            else:
                print 'Error: Must specify "month" or "year" for level argument'
        elif layout=='directed_dyad':
            if level=='year':
                df=pd.DataFrame(self.directed_dyad_year())
                df.to_csv(filename, index=False)
            elif level=='month':
                df=pd.DataFrame(self.directed_dyad_month())
                df.to_csv(filename, index=False)
            else:
                print 'Error: Must specify "month" or "year" for level argument'
        elif layout=='undirected_dyad':
            if level=='year':
                df=pd.DataFrame(self.undirected_dyad_year())
                df.to_csv(filename, index=False)
            elif level=='month':
                df=pd.DataFrame(self.undirected_dyad_month())
                df.to_csv(filename, index=False)
            else:
                print 'Error: Must specify "month" or "year" for level argument'
        else:
            print 'Error: Must specify "monadic", "directed_dyad", or "undirected_dyad" for layout argument.'
