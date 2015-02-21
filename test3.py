grocery_list=['Juice','Tomatoes',
              'Potatoes','Bananas']
print('First Item',grocery_list[0])
grocery_list[0]='Green Juice'
print('First Item',grocery_list[0])
other_events=['Wash Car','Pick up Kids']
to_do_list=[other_events,grocery_list]
print(to_do_list)
print([to_do_list[1][1]]) # This is a conflict!
grocery_list.append('Onions')
print(to_do_list)
grocery_list.insert(1,"Pickels")
print(to_do_list)
grocery_list.remove("Pickels")
print(to_do_list)
grocery_list.sort()
print(to_do_list)
grocery_list.reverse()
print(to_do_list)
del grocery_list[4]
print(to_do_list)
to_do_list2=other_events+grocery_list
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))
print(to_do_list)
pass
