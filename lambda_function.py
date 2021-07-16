'''
Lambda Functions to calculate River Details
'''


class River:
    '''
    Class for assessing river difficulty
    '''

    @staticmethod
    def km_to_miles(length):
        '''
        Function to convert km measurement to miles
        '''
        miles = int(length) / 1.6
        return miles

    @staticmethod
    def rating(length, rapids):
        '''
        Function to assess the difficulty rating of the river
        '''
        if length < 5:
            length_score = 1
        elif 6 >= length <= 10:
            length_score = 2
        elif length > 11:
            length_score = 3
        river_score = length_score + rapids
        return river_score

    @staticmethod
    def river_grade(river_score):
        '''
        Function to finalise a grade for the river
        '''
        if 2 >= river_score <= 3:
            river_rating = "Easy"
        elif 4 >= river_score <= 6:
            river_rating = "Medium"
        elif 7 >= river_score <= 8:
            river_rating = "Hard"
        else:
            river_rating = "Extreme"
        return river_rating
