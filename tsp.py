
import random

def d( cities,a, b ) :
    ''' Returns the length of the edge between city a and city b
    '''
    point1= cities[a]
    point2=cities[b]
    x1= point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    distance= (((x1-x2)**2)+((y1-y2)**2))**0.5
    return distance
    pass
    
def swap( tour, i1, i2 ) :
    ''' Swaps the values of i1 and i2 tour elements
    '''
    tour[i1], tour[i2] = tour[i2], tour[i1]
    return tour
    pass

def random_location( w, h ) :
    ''' Returns a random (x, y) coordinate where is from the range(0, w)
        and y is from the range(0, h )
    '''
    x=random.randrange(0,w)
    y=random.randrange(0,h)
    return (x,y)
    pass

def initialize_city_locations( n, w, h ) :
    ''' Returns a new list of n (x, y) pairs, where each pair is generated
        using an invocation of random_location( w, h )
    '''
    list=[]
    for i in range(0, n):
        city= random_location(w,h)
        list.append(city)
    return list
    pass

def cost( cities, tour ) :
    ''' Returns the length traveled visiting all cities in the order
        indicated by tour. That length includes the length of the
        connection from the last city back to the first city.
    '''
    n= len(cities)
    total = 0
    for i in range (0,n-1):
        yel=d(cities, tour[i], tour[i + 1])
        total = total + yel
    total = total + d(cities, tour[n-1], tour[0])
    return total
    pass

def consider( cities, tour, i1, i2 ) :
    ''' Determines whether swapping tour elements i1 and i2 produce
        a better tour.  If so, True is returned; otherwise, False is
        returned and tour is left unchanged.
    '''
    c1 = cost(cities, tour)
    new_tour = swap(tour, i1, i2)
    c2 = cost(cities, new_tour)
    if c2 < c1:
        return True
    else:
        swap(tour, i1, i2)
        return False

    pass

if ( __name__ == "__main__" ) :
    import test_tsp
    test_tsp.test_d()
    test_tsp.test_swap()
    test_tsp.test_random_location()
    test_tsp.test_initialize_city_locations()
    test_tsp.test_cost()
    test_tsp.test_consider()
