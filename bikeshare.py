import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
# months=['january', 'february', 'march', 'april', 'may', 'june']
months=['jan', 'feb', 'mar', 'apr', 'may', 'jun']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('Please input for city (chicago, new york city, washington):\n')
    city=city.lower()
    while city not in CITY_DATA.keys():
    	city= input ('Please input for a valid city name (chicago, new york city, washington):\n')
    	city=city.lower()
    	

    ''' TO DO: get user input for month (all, january, february, ... , june)
    	If user input for all, indicatest that there is no filter for month.
    '''

    #month=input('Please input for month (all, january, february, ... , june):\n')
    month=input('Please input for month (all, jan, feb, ... , jun):\n')
    month=month.lower()
    while month != 'all' and month not in months:
    	month=input ('Please input for a valid month (all, jan, feb, ... , jun):\n')
    	month=month.lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # days=['monday','tuesday','wednesday','thursday','friday', 'saturday', 'sunday']
    days=['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    day=input('Please input for day of week (all, mon, tue, ... sun):\n')

    day=day.lower()
    while day != 'all' and day not in days:
    	day=input ('Please input for a valid day of week (all, mon, tue, ... sun):\n')
    	day=day.lower()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    columns=list(df.keys())

    df['Start Time']=pd.to_datetime(df['Start Time'])

    df['month']=df['Start Time'].dt.month
    df['week_of_day']=df['Start Time'].dt.day_name().str[0:3]
    df['hour']=df['Start Time'].dt.hour

    df['Combination Station']=df['Start Station'] + ' & ' + df['End Station']

    if month != 'all':
    	df=df[df['month']==months.index(month)+1]

    if day != 'all':
    	df=df[df['week_of_day']==day.title()]


    return df, columns


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print ('The most common month is {}'.format(months[popular_month-1]))
    print ('')

    # TO DO: display the most common day of week
    popular_weekday=df['week_of_day'].mode()[0]
    print ('The most common day of week is {}.'.format(popular_weekday))
    print ('')

    # TO DO: display the most common start hour
    popular_hour=df['hour'].mode()[0]
    print ('The most common start hour is {}.'.format(popular_hour))
    print ('')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print ('The most commonly used start station is: {}'.format(popular_start_station))
    print ('')

    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print ('The most commonly used end station is: {}'.format(popular_end_station))
    print ('')

    # TO DO: display most frequent combination of start station and end station trip
    popular_combin_station=df['Combination Station'].mode()[0]
    print ('The most frequent combination of start station and end station trip is: {}'.format(popular_combin_station))
    print ('')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    travel_time=round(df['Trip Duration'].sum()/60/60, 1)
    print ('Total travel time is {} hours.'.format(travel_time))
    print ('')

    # TO DO: display mean travel time
    mean_time=round(df['Trip Duration'].mean()/60, 1)
    print ('Mean travel time is {} mins.'.format(mean_time))
    print ('')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print ('Counts of user types is:')
    print (df['User Type'].value_counts())
    print ('')

    # TO DO: Display counts of gender
    if 'Gender' in df:
    	print ('Counts of gender is:')
    	print (df['Gender'].value_counts())
    	print ('')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
    	print ('The earliest year of birth is: {}'.format(int(df['Birth Year'].min())))
    	print ('')
    	print ('The most recent year of birth is: {}'.format(int(df['Birth Year'].max())))
    	print ('')
    	print ('The most common year of birth is: {}'.format(int(df['Birth Year'].mode()[0])))
    	print ('')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_samples(df, columns):
    """Displays the data samples upon request by the users."""
    display='yes'
    while display == 'yes':
    	display=input('Do you want to see some individual data? Enter yes or no.\n')
    	if display == 'yes':
    		start_time=time.time()
    		n=1
    		while n<5:
    			print (df[columns].iloc[np.random.randint(0, df.shape[0])])
    			print ('')
    			n += 1
    	else:
    		break
    	print ('This took %s seconds.' % (time.time()-start_time))
    	print ('')

    print ('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df, columns = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_samples(df, columns)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
