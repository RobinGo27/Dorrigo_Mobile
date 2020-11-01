## SID: 500685031

## unikey: jgou4809

## Answer1.
In the declaration of a class, attributes are represented by variables, and such variables are called instance variables. Instance variables are declared inside the class but outside the other methods of the class. 

The differences between instance variables and local variables are:
1. Local variables are created when the method is called and destroyed when the method exits, while instance variables are created in the new object and are destroyed by the garbage collector when they are not referenced.

2. Local variables are declared inside the method, while instance variables are declared inside the class but outside the method.

3. Local variables can only be seen in the method in which they are declared, while instance variables can be seen by all methods in the class.

## Answer2.
I can call a function anywhere, but if I want to call a method, I must pass an object of the same datatype as the class in which the method is called. For instance, as you can see in the following code:

```python
class dorrigo_contact:
	def __init__(self, fname):
		###
		self.fname = fname
		###
	def get_first_name(self): 
		return self.fname

def first_name():
	contact = dorrigo_contact("Junbin")
	return contact.get_first_name()

print(first_name())
```

When I want to call an instance method in the dorrigo_contact object, I have to write like dorrigo_contact().get_first_name(). However, I can directly call a function by using the function name like "first_name()" in the example above. Moreover, the data in the method is implicitly passed to the object that calls the method, but all the data passed to the function is passed explicitly. Meanwhile, the class defines a datatype, and the object is an instantiation of that datatype, so when calling the instance method, the instance method can manipulate the data inside the class, which cannot be done by calling a function outside the class and the class object.

## Answer3.
1. Shallow copy: If I just want to use create_copy method to operate shallow copy, I can directly assign the original value of all instance variables to a set of new variables and use this set of new variables to create a new object. From this,I construct a new object and then insert references into it to the objects used in the original. As the code below:

```python
def create_copy(self): 
	fname = str(self.fname)
	lname = str(self.lname)
	pnumber = str(self.pnumber)
	new_chat_message = self.chat_message
	np = self.newest_position
	op = self.oldest_position
	new_object =  dorrigo_contact(fname, lname, pnumber)
	new_object.chat_message = new_chat_message
	new_object.newest_position = np
	new_object.oldest_position = op
	return new_object
```

2. Deep copy: If I want to use create_copy method to operate deep copy, I need to create new variables and set them to default values such as "" and []. Then I should divide each instance variables to different parts and move every small part to the new variables by using while loops. After that I can create the new object by using these new instance variables. From this, I construct a new object and then, recursively, insert copies of the original object into it. You can check the code of deep copy in the file dorrigo_contact.py, method create_copy().

## Answer4.

| Class |  Instance Variable | Datatype  | Mutable |
| ------------- |:-------------:| :-----:| :-----:|
| dorrigo_mobile | phone_on_or_not    | boolean 		  | No     |
| dorrigo_mobile | battery_life       | integer     	  | No     |
| dorrigo_mobile | connected_network  | boolean     	  | No     |
| dorrigo_mobile | signal_strength    | integer     	  | No     |
| dorrigo_mobile | contacts           | list           	  | Yes    |
| dorrigo_mobile | max_contacts       | integer     	  | No     |
| dorrigo_mobile | owner              | dorrigo_contact   | Yes    |
| dorrigo_contact| fname              | string            | No     |
| dorrigo_contact| lname              | string            | No     |
| dorrigo_contact| pnumber            | string            | No     |
| dorrigo_contact| chat_message       | list          	  | Yes    |
| dorrigo_contact| oldest_position    | list          	  | Yes    |
| dorrigo_contact| newest_position    | list          	  | Yes    |