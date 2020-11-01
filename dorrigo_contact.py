"""
   Dorrigo Mobile Phone Contact Class.

   INFO1110 Assignment, Semester 2, 2020.

   dorrigo_contact

   == Contact data ==
   Each dorrigo_contact stores the first name, last name and phone number of a person.
   These can be queried by calling the appropriate get method. They are updated
   with new values. The phone number can only be a 6 - 14 digit number.
   The chat history is also stored.


   == Chat history ==
   Each dorrigo_contact stores the history of chat messages related to this contact.
   Suppose there is a conversation between Angus and Beatrice:

   Angus: Man, I'm so hungry! Can you buy me a burrito?
   Beatrice: I don't have any money to buy you a burrito.
   Angus: Please? I haven't eaten anything all day.

   Each time a message is added the name of the person and the message is
   combined as above and recorded in the sequence it was received.

   The messages are stored in the instance variable. Provided for you.
   Unfortunately there are only a maximum number of messages maximum to store and no more.
   When there are more than N messages, oldest messages from this array are discarded and
   only the most recent N messages remain.

   The functions for chat history are
     add_chat_message()
     get_last_message()
     get_oldest_message()
     clear_chat_history()

   Using the above conversation as an example
     add_chat_message("Angus", "Man, I'm so hungry! Can you buy me a burrito?");
     add_chat_message("Beatrice", "I don't have any money to buy you a burrito.");
     add_chat_message("Angus", "Please? I haven't eaten anything all day.");

     get_last_message() returns "Angus: Please? I haven't eaten anything all day."
     get_oldest_message() returns "Angus: Man, I'm so hungry! Can you buy me a burrito?"

     clear_chat_history()
     get_last_message() returns None
     get_oldest_message() returns None


   == Copy of contact ==
   It is necessary to make copy of this object that contains exactly the same data.
   There are many hackers working in other parts of Dorrigo, so we cannot trust them
   changing the data. A copy will have all the private data and chat history included.


   Please implement the methods provided, as some of the marking is
   making sure that these methods work as specified.

   @author A INFO1110 tutor.
   @date September, 2020

"""


class dorrigo_contact:

    def __init__(self, fname, lname, pnumber):
        """ construct a new dorrigo_contact
            first name
            last name
            phone number
            Initialise other values to sensible default
        """
        self.fname = fname
        self.lname = lname
        self.pnumber = str(pnumber)
        self.chat_message = [None] * 20
        if fname == "Dorrigo" and lname == "Incorporated" and pnumber == "180076237867":
            self.add_chat_message("Dorrigo", "Thank you for choosing Dorrigo products")
        self.oldest_position = [0]
        self.newest_position = [0]

    def get_first_name(self):
        """ return the first name of the contact """
        return self.fname

    def get_last_name(self):
        """ return the last name of the contact """
        return self.lname

    def get_phone_number(self):
        """ return the phone number of the contact as a string """
        self.pnumber = str(self.pnumber)
        return self.pnumber

    def update_first_name(self, first_name):
        """ if first_name is None the method will do nothing and return.
            The name will only update if the datatype is appropriate
        """
        if self.fname == None:
            return
        elif type(self.fname) == str and len(self.fname) > 0:
            self.fname = first_name

    def update_last_name(self, last_name):
        """ if last_name is None the method will do nothing and return
            The name will only update if the datatype is appropriate
        """
        if self.lname == None:
            return
        elif type(self.lname) == str and len(self.lname) > 0:
            self.lname = last_name

    def update_phone_number(self, number):
        """ only allows integer numbers (long type) between 6 and 14 digits
           no spaces allowed, or prefixes of + symbols
           leading 0 digits are allowed
           return True if successfully updated
           if number is None, number is set to an empty string and the method returns False
        """
        if type(number) == int:
            if len(str(number)) >= 6 and len(str(number)) <= 14:
                self.pnumber = str(number)
                return True
            else:
                return False
        elif type(number) == str:
            if number.isdigit() == True:
                if len(number) >= 6 and len(number) <= 14:
                    self.pnumber = str(number)
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def add_chat_message(self, who_said_it, message):
        """ add a new message to the chat
           The message will take the form
           who_said_it + ": " + message

           if the history is full, the oldest message is replaced
           Hint: keep track of the position of the oldest or newest message!
           always returns True
        """
        m = str(who_said_it) + ": " + str(message)
        if None in self.chat_message:
            i = 0
            while i < 20:
                if self.chat_message[i] == None:
                    self.chat_message[i] = m
                    self.oldest_position = [0]
                    self.newest_position = [i]
                    return True
                    break
                else:
                    i = i + 1
        else:
            if self.oldest_position[0] < 19:
                self.chat_message[self.oldest_position[0]] = m
                self.newest_position[0] = self.oldest_position[0]
                self.oldest_position[0] = self.oldest_position[0] + 1
                return True
            elif self.oldest_position[0] == 19:
                self.chat_message[self.oldest_position[0]] = m
                self.newest_position[0] = self.oldest_position[0]
                self.oldest_position = [0]
                return True

    def clear_chat_history(self):
        """ after this, both last and oldest message should be referring to index 0
           all entries of chat history are set to None
           always returns True
        """
        self.chat_message = [None] * 20
        self.oldest_position = [0]
        self.newest_position = [0]
        return True

    def get_last_message(self):
        """ returns the last message
               if no messages, returns None
        """
        if self.chat_message == ([None] * 20):
            return None
        else:
            return (self.chat_message[self.newest_position[0]])

    def get_oldest_message(self):
        """ returns the oldest message in the chat history
           depending on if there was ever MAXIMUM_CHAT_HISTORY messages
           1) less than MAXIMUM_CHAT_HISTORY, returns the first message
           2) more than MAXIMUM_CHAT_HISTORY, returns the oldest
           returns None if no messages exist
        """
        if self.chat_message == ([None] * 20):
            return None
        else:
            return (self.chat_message[self.oldest_position[0]])

    def create_copy(self):
        """ creates a copy of this contact
           returns a new dorrigo_contact object with all data same as the current object
        """
        fname = str(self.fname)
        lname = str(self.lname)
        pnumber = str(self.pnumber)
        chat_message = list(self.chat_message)
        np = list(self.newest_position)
        op = list(self.oldest_position)
        new_fname = ""
        new_lname = ""
        new_pnumber = ""
        new_chat_message = []
        new_np = []
        new_op = []
        i = 0
        while i < len(fname):
            new_fname = new_fname + fname[i]
            i = i + 1
        i = 0
        while i < len(lname):
            new_lname = new_lname + lname[i]
            i = i + 1
        i = 0
        while i < len(pnumber):
            new_pnumber = new_pnumber + pnumber[i]
            i = i + 1
        i = 0
        while i < len(chat_message):
            new_chat_message.append(chat_message[i])
            i = i + 1
        i = 0
        while i < len(np):
            new_np.append(np[i])
            i = i + 1
        i = 0
        while i < len(op):
            new_op.append(op[i])
            i = i + 1
        new_object = dorrigo_contact(new_fname, new_lname, new_pnumber)
        new_object.chat_message = new_chat_message
        new_object.newest_position = new_np
        new_object.oldest_position = op
        return new_object

    def print_messages_oldest_to_newest(self):
        """ -- NOT TESTED --
           You can impelement this to help with debugging when failing ed tests
           involving chat history. You can print whatever you like
           Implementers notes: the format is printf("%d %s\n", index, line);
        """
        pass
