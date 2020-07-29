class Time_Cal:

    def __init__(self, hour=0, minute=0, seg=0):
        if (isinstance(hour, int)) and (isinstance(minute, int)) and (isinstance(seg, int)):
            self.hour = hour
            self.minute = minute
            self.seg = seg
        else:
            raise TypeError("Hour, Minute and Second can only be int values!")

    def __add_sub(self, time2, type):
        time1_seg = self.hour * 3600 + self.minute * 60 + self.seg
        if isinstance(time2, Time_Cal):
            time2_seg = time2.hour * 3600 + time2.minute * 60 + time2.seg
        else:
            time2_seg = time2

        if type == "addition":
            time_seg = time1_seg + time2_seg
        elif type == "substraction":
            # absolute value of the rest, always return a positive value
            time_seg = abs(time1_seg - time2_seg)
        elif type == "addition_int":
            time_seg = time1_seg + time2_seg
        elif type == "substraction_int":
            time_seg = abs(time1_seg - time2_seg)

        else:
            # Anything that is not + or -, raise error
            raise TypeError("Unknown operation!")

        final_hour = time_seg // 3600
        final_minute = (time_seg % 3600) // 60
        final_seg = time_seg % 60
        return Time_Cal(final_hour, final_minute, final_seg)

    def __add__(self, other):
        if isinstance(other, Time_Cal):
            return self.__add_sub(other, "addition")
        elif isinstance(other, int):
            return self.__add_sub(other, "addition_int")
        else:
            raise TypeError("The object is not Time_Cal")

    def __sub__(self, other):
        if isinstance(other, Time_Cal):
            return self.__add_sub(other, "substraction")
        elif(isinstance(other, int)):
            return self.__add_sub(other, "substraction_int")
        else:
            raise TypeError("The object is not Time_Cal")

    def __mul__(self, value):
        if isinstance(value, int):
            time_seg = self.hour * 3600 + self.minute * 60 + self.seg
            time_seg *= value
        else:
            raise TypeError("The value is not int!")
        final_hour = time_seg // 3600
        final_minute = (time_seg % 3600) // 60
        final_seg = time_seg % 60
        return Time_Cal(final_hour, final_minute, final_seg)

    def __str__(self):
        return str(self.hour) + ":" + str(self.minute) + ":" + str(self.seg)
