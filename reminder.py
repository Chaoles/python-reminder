#!/usr/bin/env python
import subprocess
from time import sleep


"""
Copyright (C) 2017  Puskar Adhikari

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

def main():
    
    ### Pulling number of reminders
    print "Enter number of Reminders:",
    reminders = int(raw_input())

    ### Pulling messages for reminders
    reminders_list = []
    for numbers in range(reminders):
        print "Enter message number",numbers+1,": ",
        reminders_list.append(raw_input())
    
    print "Enter the interval time(in minutes): ",
    interval_time = int(raw_input())

    ### Sending messages after user given intervals
    for i in range(reminders):
        sleep(interval_time * 60)
        sendreminders(reminders_list[i])
        subprocess.call(["aplay", "sound.wav"])


def sendreminders(messages):
    subprocess.Popen(['notify-send', messages])
    return

main()
