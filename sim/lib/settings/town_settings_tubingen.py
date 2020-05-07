import numpy as np

'''
Settings for town generation
'''

town_name = 'Tubingen' 

# Make sure to download country-specific population density data
# from https://data.humdata.org/organization/facebook
population_path='lib/data/population/population_deu_2019-07-01.csv' # Population density file

sites_path='lib/data/queries/' # Directory containing OSM site query details
bbox = (48.4900, 48.5485, 9.0224, 9.1061) # Coordinate bounding box

# Population per age group in the region
population_per_age_group = np.array([
    13416, # 0-4
    18324, # 5-14
    67389, # 15-34
    75011, # 35-59
    41441, # 60-79
    11750])# 80+

town_population = 90546 # Population of the town of interest
region_population = population_per_age_group.sum()

# Information about household structure (set to None if not available)
household_info = {
    'size_dist' : [41.9, 33.8, 11.9, 9.1, 3.4], # distribution of household sizes (1-5 people)
    'soc_role' : {
        'children' : [1, 1, 3/20, 0, 0, 0], # age groups 0,1,2 can be children 
        'parents' : [0, 0, 17/20, 1, 0, 0], # age groups 2,3 can be parents
        'elderly' : [0, 0, 0, 0, 1, 1] # age groups 4,5 are elderly
    }
}

