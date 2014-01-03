lists=[20,12,34,12,24,34,55,27]
print list(set(lists))
print sorted(set(lists),key=lists.index)

print set('abc').intersection('cbs')


s = set([3,5,9,10])
t = set([3,6,7,10])
##s.intersection_update(t)
##print s,t
##
##s.update(t)
##print s,t

##s.difference_update(t)
##print s,t

s.symmetric_difference_update(t)
print s,t


theString = 'saaaay yes no yaaaass'
print theString.strip('say') 
print theString.strip('say ') #say后面有空格 
print theString.lstrip('say') 
print theString.rstrip('say') 

