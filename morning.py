
#1. Waking Up
def wake_up(day_of_week):
    if ((day_of_week.lower() == "saturday") or (day_of_week.lower() == "sunday")):
      return "Go back to bed"
    else:
      return "Stop hitting snooze"

#2. The Commute
def commute(weather, mins_until_work):
    if ((mins_until_work<=10) or (weather.lower()=="rainy")):
      return "Better take the car"
    elif ((mins_until_work>30) and (weather.lower()=="sunny")):
      return "Enjoy a bike ride!"
    else:
      return "Hop on the bus"

#3. Coffee Buzz

def coffee(number):
  if (number>=100):
    return "Time for a triple shot espresso"
  elif ((number<100) and (number>=50)):
    return "Go for a large black coffee"
  elif ((number<50) and (number>0)):
    return "A latte will serve you well"
  elif (number == 0):
    return "You have reached the Nirvana of 21st century communication!"
  elif (number < 0):
    return "Is this a new Gmail feature?"