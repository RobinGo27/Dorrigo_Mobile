"""
 * Dorrigo Mobile Phone Class.
 *
 * INFO1110 Assignment, Semester 2, 2020.
 *
 * dorrigo_mobile
 * In this assignment you will be creating an Dorrigo Mobile Phone as part of a simulation.
 * The Mobile phone includes several attributes unique to the phone and has simple functionality.
 * You are to complete 2 classes. dorrigo_mobile and dorrigo_contact
 *
 * The phone has data
 *  Information about the phone state.
 *    If it is On/Off
 *    Battery level
 *    If it is connected to network.
 *    Signal strength when connected to network
 *  Information about the current owner saved as contact information.
 *    First name
 *    Last name
 *    Phone number
 *  A list of 10 possible contacts.
 *    Each contact stores first name, last name, phone number and chat history up to 20 messages
 *
 * The phone has functionality
 *  Turning on the phone
 *  Charging the phone. Increase battery level
 *  Change battery (set battery level)
 *  Use phone for k units of battery (decreases battery level by k)
 *  Search/add/remove contacts
 *
 * Attribute features
 *  if the phone is off. It is not connected.
 *  if the phone is not connected there is no signal strength
 *  the attribute for battery life has valid range [0,100]. 0 is flat, 100 is full.
 *  the attribute for signal strength has a valid range [0, 5]. 0 is no signal, 5 is best signal.
 *
 * Please implement the methods provided, as some of the marking is
 * making sure that these methods work as specified.
 *
 * @author An INFO1110 tutor.
 * @date September, 2020
 *
"""

from dorrigo_contact import dorrigo_contact


class dorrigo_mobile:

    def __init__(self, max_contacts):
        """
        Every phone manufactured has the following attributes

         the phone is off
         the phone has battery life 25
         the phone is not connected
         the phone has signal strength 0
         Each of the contacts stored in the array contacts has a None value

         the owner first name "Dorrigo"
         the owner last name is "Incorporated"
         the owner phone number is "180076237867"
         the owner chat message should have only one message
                 "Thank you for choosing Dorrigo products"
        """
        # contacts =
        self.phone_on_or_not = False
        self.battery_life = 25
        self.connected_network = False
        self.signal_strength = 0
        self.max_contacts = max_contacts
        self.contacts = [None] * (self.max_contacts + 1)  # 1 for the owner
        self.owner = dorrigo_contact(fname="Dorrigo", lname="Incorporated", pnumber="180076237867")
        self.contacts[0] = self.owner

    def get_copy_of_owner_contact(self):
        """  returns a copy of the owner contact details
               return None if the phone is off
        """

        if self.phone_on_or_not == False:
            return None
        else:
            owner_copy = self.contacts[0].create_copy()
            return owner_copy

    def add_contact(self, contact):
        """ only works if phone is on
           will add the contact in the array only if there is space and does not exist
           The method will find an element that is None and set it to be the contact.
           returns True if successful
        """
        if self.phone_on_or_not == False:
            return False
        else:
            if contact == None:
                return False
            elif None not in self.contacts:
                return False
            else:
                # to see if the contact exists
                j = 0
                while j < len(self.contacts):
                    if self.contacts[j] != None:
                        if self.contacts[j].fname == contact.fname and self.contacts[j].lname == contact.lname and \
                                self.contacts[j].pnumber == contact.pnumber:
                            return False
                        else:
                            j = j + 1
                    else:
                        j = j + 1
                i = 0
                while i < len(self.contacts):
                    if self.contacts[i] == None:
                        self.contacts[i] = contact
                        return True
                        break
                    else:
                        i = i + 1

    def remove_contact(self, contact):
        """ only works if phone is on
           find the dorrigo_contact object and set the array element to None
            return True on successful remove
        """
        if self.phone_on_or_not == False:
            return False
        else:
            if contact == None:
                return False
            else:
                i = 0
                found = False
                while i < len(self.contacts):
                    if self.contacts[i] != None:
                        if self.contacts[i].fname == contact.fname and self.contacts[i].lname == contact.lname and \
                                self.contacts[i].pnumber == contact.pnumber:
                            self.contacts[i] = None
                            found = True
                            return True
                            break
                        else:
                            i = i + 1
                    else:
                        i = i + 1
                if found == False:
                    return False

    def get_number_of_contacts(self):
        """ only works if phone is on
            returns the number of contacts, or -1 if phone is off
        """
        if self.phone_on_or_not == False:
            return -1
        else:
            num = 0
            i = 0
            while i < len(self.contacts):
                if self.contacts[i] != None:
                    i = i + 1
                    num = num + 1
                else:
                    i = i + 1
            return num - 1  # except the owner

    def search_contact(self, name):
        """ only works if phone is on
           returns a list of all contacts that match first name OR last name
           if phone is off, or no results, None is returned
        """
        if self.phone_on_or_not == False:
            return None
        else:
            name_list = []
            i = 1
            while i < len(self.contacts):
                if self.contacts[i] != None:
                    if self.contacts[i].lname == name or self.contacts[i].fname == name:
                        name_list.append(self.contacts[i])
                        i = i + 1
                    else:
                        i = i + 1
                else:
                    i = i + 1
            if len(name_list) == 0:
                return None
            else:
                return name_list

    def is_phone_on(self):
        """ returns True if phone is on
        """
        if self.phone_on_or_not == True:
            return True
        else:
            return False

    def set_phone_on(self, on):
        """
            set the on status based on the boolean input
            when phone turns on, it costs 5 battery for startup. network is initially disconnected
            when phone turns off it costs 0 battery, network is disconnected
            always return True if turning off
            return False if do not have enough battery level to turn on
            return True otherwise
        """
        if on == True:
            if self.phone_on_or_not == False:
                self.battery_life = self.battery_life - 5
                if self.battery_life <= 0:
                    self.battery_life = self.battery_life + 5
                    self.phone_on_or_not = False
                    return False
                else:
                    self.connected_network = False
                    self.phone_on_or_not = True
                    return True
            else:
                return True
        else:
            if self.phone_on_or_not == True:
                self.phone_on_or_not = False
                self.connected_network = False
                return True
            else:
                return True

    def get_battery_life(self):
        """ Return the battery life level as an integer. if the phone is off, zero is returned.
        """
        if self.phone_on_or_not == False:
            return 0
        else:
            return int(self.battery_life)

    def change_battery(self, new_battery_level):
        """ Change battery of phone.
           On success. The phone is off and new battery level adjusted and returns True
           If new_battery_level is outside manufacturer specification of [0,100], then
           no changes occur and returns False.
        """
        if new_battery_level < 0 or new_battery_level > 100:
            return False
        else:
            self.battery_life = new_battery_level
            self.phone_on_or_not = False
            return True

    def is_connected_network(self):
        """ only works if phone is on.
            returns True if the phone is connected to the network
        """
        if self.phone_on_or_not == True:
            if self.connected_network == True:
                return True
            else:
                return False
        else:
            return False

    def disconnect_network(self):
        """ only works if phone is on.
            when disconnecting, the signal strength becomes zero
            always returns True
        """
        if self.phone_on_or_not == True:
            self.signal_strength = 0
            return True
        else:
            return True

    def connect_network(self):
        """ only works if phone is on.
           Connect to network
           if already connected do nothing and return True
           if connecting:
            1) signal strength is set to 1 if it was 0
            2) signal strength will be the previous value if it is not zero
            3) it will cost 2 battery life to do so
           returns the network connected status
        """
        if self.phone_on_or_not == True:
            if self.connected_network == True:
                return True
            else:
                if self.signal_strength == 0:
                    self.signal_strength = 1
                    self.battery_life = self.battery_life - 2
                    if self.battery_life <= 0:
                        self.battery_life = 0
                        self.connected_network = False
                        return self.connected_network
                    else:
                        self.connected_network = True
                        return self.connected_network
                else:
                    self.signal_strength = self.signal_strength
                    self.battery_life = self.battery_life - 2
                    if self.battery_life <= 0:
                        self.battery_life = 0
                        self.connected_network = False
                        return self.connected_network
                    else:
                        self.connected_network = True
                        return self.connected_network
        else:
            return False

    def get_signal_strength(self):
        """ only works if phone is on.
           returns a value in range [1,5] if connected to network
           otherwise returns 0
        """
        if self.phone_on_or_not == True:
            if self.connected_network == True:
                if self.signal_strength >= 1 and self.signal_strength <= 5:
                    return self.signal_strength
                else:
                    return 0
            else:
                return 0
        else:
            return 0

    def set_signal_strength(self, new_strength):
        """ only works if phone is on.
           sets the signal strength and may change the network connection status to on or off
           signal of 0 disconnects network
           signal [1,5] can connect to network if not already connected
           if the signal is set outside the range [0,5], nothing will occur and will return False
           returns True on success
        """
        if self.phone_on_or_not == True:
            if new_strength < 0 or new_strength > 5:
                return False
            else:
                self.signal_strength = new_strength
                if self.signal_strength == 0:
                    self.connected_network = False
                    return True
                else:
                    self.connected_network = True
                    return True
        else:
            return False

    def charge_phone(self):
        """ each charge increases battery level by 10
           the phone has overcharge protection and cannot exceed 100
           returns True if the phone was charged by 10, otherwise False
        """
        self.battery_life = self.battery_life + 10
        if self.battery_life > 100:
            self.battery_life = 100
            return False
        else:
            return True

    def use_phone(self, k):
        """ Use the phone which costs k units of battery life.
           if the activity exceeds the battery life, the battery automatically
           becomes zero and the phone turns off.
           returns True on successful use (not partial)
        """
        if (type(k) == int or type(k) == float) and k >= 0:
            if k > self.battery_life:
                self.battery_life = 0
                self.phone_on_or_not = False
                return False
            else:
                self.battery_life = self.battery_life - k
                return True
