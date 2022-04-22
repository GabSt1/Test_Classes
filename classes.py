class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        self.__tvChannel = int = Television.MIN_CHANNEL
        self.__tvVolume = int = Television.MIN_VOLUME
        self.__tvStatus = 'False'

    def power(self) -> None:

        '''
        Method to turn the TV on or off
        '''
        if self.__tvStatus == 'False':
            self.__tvStatus = 'True'
        elif self.__tvStatus == 'True':
            self.__tvStatus = 'False'

    def channel_up(self) -> None:

        '''
        Method to change the channel up
        '''
        if self.__tvStatus == 'True' and self.__tvChannel < Television.MAX_CHANNEL:
            self.__tvChannel += 1

        elif self.__tvStatus == 'True' and self.__tvChannel == Television.MAX_CHANNEL:
            self.__tvChannel = Television.MIN_CHANNEL

    def channel_down(self) -> None:

        '''
        Method to change the channel down
        '''
        if self.__tvStatus == 'True' and self.__tvChannel > Television.MIN_CHANNEL:
            self.__tvChannel -= 1
            
        elif self.__tvStatus == 'True' and self.__tvChannel < Television.MIN_CHANNEL:
            self.__tvChannel = Television.MAX_CHANNEL

    def volume_up(self) -> None:

        '''
        Method to turn the volume up
        '''
        if self.__tvStatus == 'True' and self.__tvVolume < Television.MAX_VOLUME:
            self.__tvVolume += 1

        elif self.__tvStatus == 'True' and self.__tvVolume == Television.MAX_VOLUME:
            self.__tvVolume = Television.MAX_VOLUME

    def volume_down(self) -> None:

        '''
        Method to turn the volume down
        '''
        if self.__tvStatus == 'True' and self.__tvVolume > Television.MIN_VOLUME:
            self.__tvVolume -= 1
            
        elif self.__tvStatus == 'True' and self.__tvVolume == Television.MIN_VOLUME:
            self.__tvVolume = Television.MIN_VOLUME

    def __str__(self):
        '''
        Returns the status of the TV, and what the values of the channel and volume are
        '''
        return f'TV status: Is on = {self.__tvStatus}, Channel = {self.__tvChannel}, Volume = {self.__tvVolume}'
