#tp
import numpy
import random
import pylab
count = 0
Acount = []
som = 0
media = 0.0
class GameOfLife:

   def __init__(self, N=100, T=200):
      """ Set up Conway's Game of Life. """
      global count
      # Here we create two grids to hold the old and new configurations.
      # This assumes an N*N grid of points.
      # Each point is either alive or dead, represented by integer values of 1 and 0, respectively.
      self.N = N
      self.old_grid = numpy.zeros(N*N, dtype='i').reshape(N,N)
      self.new_grid = numpy.zeros(N*N, dtype='i').reshape(N,N)
      self.T = T # The maximum number of generations

      # Set up a random initial configuration for the grid.
      for i in range(0, self.N):
         for j in range(0, self.N):
            if(random.randint(0, 100) < 15):
               self.old_grid[i][j] = 1
               count += 1
               Acount.append(count)
            else:
               self.old_grid[i][j] = 0
      
   def live_neighbours(self, i, j):
      """ Count the number of live neighbours around point (i, j). """
      s = 0 # The total number of live neighbours.
      # Loop over all the neighbours.
      for x in [i-1, i, i+1]:
         for y in [j-1, j, j+1]:
            if(x == i and y == j):
               continue # Skip the current point itself - we only want to count the neighbours!
            if(x != self.N and y != self.N):
               s += self.old_grid[x][y]
            # The remaining branches handle the case where the neighbour is off the end of the grid.
            # In this case, we loop back round such that the grid becomes a "toroidal array".
            elif(x == self.N and y != self.N):
               s += self.old_grid[0][y]
            elif(x != self.N and y == self.N):
               s += self.old_grid[x][0]
            else:
               s += self.old_grid[0][0]
      return s

   def play(self):
      """ Play Conway's Game of Life. """
      global count , som,media
      # Write the initial configuration to file.
      pylab.pcolormesh(self.old_grid)
      pylab.colorbar()
      pylab.savefig("D:\\Backam\\Tommy\\Py\\generation0.png")
      pylab.contourf(self.old_grid)
      pylab.savefig("D:\\Backam\\Tommy\\Py\\polarInitial.png")
      pylab.plot(Acount)
      pylab.xlabel("Generazioni")
      pylab.xlabel("Numero delle cellule")
      pylab.savefig("D:\\Backam\\Tommy\\Py\\count0.png")
      t = 1 # Current time level
      #write_frequency = 1 # How frequently we want to output a grid configuration.
      while t <= self.T: # Evolve!
         print ("GENERAZIONE N°%d" % t)
         # Loop over each cell of the grid and apply Conway's rules.
         for i in range(self.N):
            for j in range(self.N):
               live = self.live_neighbours(i, j)
               if(self.old_grid[i][j] == 1 and live < 2):
                  self.new_grid[i][j] = 0 # Dead from starvation.
                  count -= 1
                  Acount.append(count)
               elif(self.old_grid[i][j] == 1 and (live == 2 or live == 3)):
                  self.new_grid[i][j] = 1 # Continue living.
               elif(self.old_grid[i][j] == 1 and live > 3):
                  self.new_grid[i][j] = 0 # Dead from overcrowding.
                  count -= 1
                  Acount.append(count)
               elif(self.old_grid[i][j] == 0 and live == 3):
                  self.new_grid[i][j] = 1 # Alive from reproduction.
                  count += 1
                  Acount.append(count)
         pylab.pcolormesh(self.old_grid)
         pylab.colorbar()
         pylab.savefig("D:\\Backam\\Tommy\\Py\\generations.png")
         pylab.clf()
         pylab.contourf(self.old_grid)
         pylab.colorbar()
         pylab.savefig("D:\\Backam\\Tommy\\Py\\polars.png")
         pylab.clf()
         pylab.plot(Acount)
         pylab.xlabel("Generazioni")
         pylab.xlabel("Numero delle cellule")
         pylab.savefig("D:\\Backam\\Tommy\\Py\\counts.png")
         pylab.clf()
         
         #if(t % write_frequency == 0):
            #pylab.pcolormesh(self.new_grid)
            #pylab.savefig("C:\\Users\\ANGELINA\\Desktop\\Life\\generation0.png")

         self.old_grid = self.new_grid.copy()
         t += 1
      for c in Acount:
          som += c
      media = som/Acount.__len__()
      print("La media delle cellule è %d"%media)
      pylab.plot(Acount)
      pylab.xlabel("Generazioni")
      pylab.xlabel("Numero delle cellule")
      pylab.plot(media)
      pylab.savefig("D:\\Backam\\Tommy\\Py\\media.png")
      pylab.clf()
if(__name__ == "__main__"):
    a = input("Premi un tasto per iniziare la simulazione!")
    while a != "11":
        a = input("Immetti la password : ")
    a = int(input("Immettere numero di spegnimento : "))
    game = GameOfLife(N = 100, T = a)
    game.play()