import playhistory
import song
from song import Song
from binary_search_tree import *
from stack import Stack
from playhistory import *


class MyPlayer:

    def __init__(self):
        """

        :return:
        """
        self.songList = []
        self.is_sorted = False
        self.yearMemory = {}
        self.playHistory = LP_List()
        # TODO: Modify the above attribute for Task 6

    def loadLibrary(self, filename: str):
        """
        :param filename: takes in a text file as an input
        :return: self.songList , class instance of the entire list of songs
        """
        song_loader = open(filename, 'r')  # opens file in read mode

        for line in song_loader:
            splitter = line.strip().split('|')
            # strips whitespace, splits line into sections where '|' character is, allows for variable assignment

            # ----- Variable Assignment -----

            artist_name = splitter[0]

            song_title = splitter[1]

            song_id = splitter[2]

            duration = float(splitter[3])

            year = int(splitter[4])

            # creates a song object to be appended to the class instance 'songList'
            song_entry = Song(artist_name, song_title, song_id, duration, year)

            self.songList.append(song_entry)  # append song object to list

        return self.songList  # return list of songs

    def quick_sort_helper(self, songList, low, high):
        """

        :return: breaks down array size for sorting
        """
        if low < high:
            split = self.partiton(songList, low, high)

            self.quick_sort_helper(songList, low, split - 1)
            self.quick_sort_helper(songList, split + 1, high)

    def partiton(self, songList, low, high):

        tp = songList[low]  # turning point to be compared to the rest of the values

        lefthand = low + 1  # left index representing the first item in the list to begin comparison
        righthand = high  # right index representing the final item in the list to begin comparison

        done = False  # variable controlling sorting logic ; if true list is sorted
        while done is not True:

            while lefthand <= righthand and songList[lefthand].year <= tp.year:
                # moves pointer if left index is less than right index & year of the current index
                # is less than the TP value
                lefthand += 1

            while righthand >= lefthand and songList[righthand].year >= tp.year:  # moves right-hand to the left if its
                # year value is less than that of the turning point
                righthand -= 1

            if righthand < lefthand:  # Sorting is complete if right hand position is less than the left hand position

                done = True  # Sorting is complete condition

            else:

                temp = songList[lefthand]  # assign left index as temporary value
                songList[lefthand] = songList[righthand]  # replace the left hand value with the right hand value
                songList[righthand] = temp  # set the right hand value to the temp (old left hand value)

        songList[low] = songList[righthand]  # low marker replaced with right hand value
        songList[righthand] = tp  # Move the pivot element to its correct position

        return righthand

    def quickSort(self):
        """

        :return: True if quicksort is successfully preformed
        """

        self.quick_sort_helper(self.songList, 0, len(self.songList) - 1)

        self.is_sorted = True

        return self.is_sorted

    def playSong(self, name: str):
        """
        :param name: takes in the title of a song
        :return: if title is in the song list it will be played
        """
        songList = self.songList

        for curr_song in songList:

            if curr_song.song_title == name:

                self.playHistory.append(curr_song)

                Song.play(curr_song)

                return

        raise AttributeError('ERROR: Song Object: "%s" is not in library' % name)

    def getLastPlayed(self):

        """
        :param: lsp = variable used to call and return the last song played
        :return: None if no previous song is played ; otherwise return last song played
        """

        return self.playHistory.getlast()

    def hashfunction(self, song):
        return song.year

    def buildYearMemory(self):
        """

        :return: None, builds hashtable
        """

        for song in self.songList:  # iterates each song item
            key = self.hashfunction(song)  # creates a 'key' object for building hashtable

            if key not in self.yearMemory:  # if the key does not have an associated BST object
                self.yearMemory[key] = BinarySearchTree()  # create BST object

            self.yearMemory[key].put(song.song_title, song)  # put song title and object into BST

    def getYearMemory(self, year, title):
        """

        :param year: takes in year to reference Binary Search Tree in hashtable
        :param title: Key to search by -> will traverse BST in order: 0(n) worst case, 0(log n) avg case
        :return: returns the song and how many steps to reach it in a dict; if song or year not in memory return None
        """

        steps = 0  # Number of steps used to search for the song
        the_song = None  # The song

        if year not in self.yearMemory:  # year not present in hash table
            print('year not in mem')
            return {"steps": None, "song": None}

        if year in self.yearMemory:  # year is present in hash table

            result = self.yearMemory[year].search(title, self.yearMemory[year].root)  # call BST search function

            if result is not None:  # item exists in the list
                # ----- Variable Assignment -----
                the_song = result["song"]
                steps = result["steps"]
                return {"steps": steps, "song": the_song}  # returns dict containing steps and the song

            # Return None if the year or song is not found
            return None

    def getSong(self, year, title):
        """
        :param year:  takes in year
        :param title:  takes in title -> this is what we will use the search
        :return:  returns steps and the song -> None if not found
        """
        steps = 0  # Number of steps used to search for the song
        the_song = None  # The song

        for song in self.songList:  # iterate over each song element

            if song.song_title == title:  # stop condition -> song is found
                the_song = song
                steps += 1  # increment steps -> final comparison
                break
            else:
                steps += 1  # increment steps when not found

        return {"steps": steps, "song": the_song}

# NO MORE TESTING CODE BELOW!
# TO TEST YOUR CODE, MODIFY test_my_player.py
