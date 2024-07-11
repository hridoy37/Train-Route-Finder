from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Train, Station, TrainRoute
from .serializers import TrainSerializer, StationSerializer, TrainRouteSerializer
import heapq


class StationList(APIView):
    def get(self,request):
        stations = Station.objects.all()
        station = StationSerializer(stations,many = True)
        return Response(station.data)
    
    

class LowCostPath(APIView):
    def get(self, request):

        trains = Train.objects.all()
        serializer = TrainSerializer(trains, many=True)

        train_dict = {}


        for x in serializer.data:
            train_dict[x["id"]] = x['name']
        train_dict[-1] = "starting"
        
        # print(train_dict)




        routes = TrainRoute.objects.all()
        route = TrainRouteSerializer(routes, many=True)

        stations = Station.objects.all()
        station = StationSerializer(stations,many = True)

        station_dict = {}
        for x in station.data:
            station_dict[x["id"]] = x['name']


        #calculate highest station id
        highest =  0
        for x in station.data:
            if(x['id']>highest):
                highest = x['id']


        #initialize a adjacency list 
        arr = [[0,0]]
        g = [[] for _ in range(highest + 1)]


        
        #initial cost to reach each station from source station
        dis = [[999999999,-1,-1] for _ in range(highest+1)]



        for x in route.data:
            u = x['from_station']
            v = x['to_station']
            fare = int(float(x['fare']))
            train = x['train']
            g[u].append([v,fare,train])
            g[v].append([u,fare,train])
      
        
        source = int(request.GET.get('source','1'))
        destination = int(request.GET.get('destination','1'))
        priority_q = []
        heapq.heapify(priority_q)



        #first parameter -> total fare from source
        #second parameter -> current station
        #third -> previous station
        #forth -> train used to reach here from previous station

        heapq.heappush(priority_q,(0,source,-1,-1))
        dis[source] = [0,-1,-1]


        while(True):
            if not priority_q:
                break
            node = heapq.heappop(priority_q)
            st = node[1]
            # print(st)
            for x in g[st]:
                child = x[0]
                cost = x[1]
                if(child == source):
                    continue
                if(dis[child][0]>dis[st][0]+cost or  dis[child][1] == -1):
                    dis[child] = [dis[st][0]+cost,st,x[2]]
                    heapq.heappush(priority_q,(dis[st][0]+cost,child,st,x[2]))
        

        if(dis[destination][0] == 999999999 and destination != source):
            response_data = {
                "error": "No path found between source and destination."
            }
            return Response(response_data)
        
        # retrive shortest path from source to destination
        shortest_path = []
        shortest_path.append([station_dict[destination],train_dict[dis[destination][2]]])
        temp = dis[destination][0]
        while(True):
            if destination <= -1 :
                break
            destination = dis[destination][1]
            # print(destination)
            if destination <= -1:
                break

            shortest_path.append([station_dict[destination],train_dict[dis[destination][2]]])

        shortest_path.reverse()
        # print(shortest_path)
        response_data = {
            "path": shortest_path,
            "cost" : temp
        }
        
            
        return Response(response_data)


    
