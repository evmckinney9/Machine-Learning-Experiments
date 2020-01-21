from ML_Algorithms.kmeans.image_scanner import *
import random
from math import sqrt

#distance between colors
def distance(pix1,pix2):
    d =0
    for i in range(len(pix1)):
        d += (pix2[i]-pix1[i])**2
    return sqrt(d)


def runner(numcolors, picnum):
    fn = "image" + picnum +".jpg"
    #setup vars
    k=numcolors
    filename = fn
    im = getImage(filename)
    pixelarray = getRGB(im)
    imgdimensions = getDimensions(im)

    #select k points randomly with no repeats
    centroids = []
    randX = random.sample(range(imgdimensions[0]),k)
    randY = random.sample(range(imgdimensions[1]),k)
    for i in range(k):
        krandomX = randX[i]
        krandomY = randY[i]
        centroids.append(pixelarray[krandomX,krandomY])

    dictClusters = {}
    for i in range(k):
        dictClusters[i] = []

    #repeat with new centroids until centroids stop changing
    max_iters = 10
    nomovement = False
    repeats = 0
    while (repeats < max_iters and not nomovement):
        #group all pixels to their nearest centroid
        #for each pixel for each centroid group it with the min distance
        for x in range(imgdimensions[0]):
            for y in range(imgdimensions[1]):
                c_topair = 0
                minDistance = 442 #441.6 is the distance between (225,225,255) and (0,0,0)
                for i in range(k):
                    newDistance = distance(pixelarray[x,y],centroids[i])
                    if newDistance<minDistance:
                        minDistance = newDistance
                        c_topair = i
                dictClusters[c_topair].append(pixelarray[x,y])
        #find the center for each cluster
        nomovement = True
        for i in range(k):
            rtotal = 0
            gtotal =0
            btotal = 0
            count =0
            clusterpoints = dictClusters[i]
            for point in clusterpoints:
                rtotal += point[0]
                gtotal += point[1]
                btotal += point[2]
                count += 1
            rtotal = rtotal/count
            gtotal = gtotal/count
            btotal = btotal/count
            #check to see if centroid changed
            check1 = round(rtotal) == round(centroids[i][0])
            check2 = round(gtotal) == round(centroids[i][1])
            check3 = round(btotal) == round(centroids[i][2])
            nomovement = True and nomovement
            nomovement = (check1 and check2 and check3)
            #set the centroid to the center
            centroids[i] = (rtotal,gtotal,btotal)
            dictClusters[i] = []   
        repeats+=1
        
    #set pixel to the same as the centroids for the cluster it is in
    for x in range(imgdimensions[0]):
            for y in range(imgdimensions[1]):
                c_toset = 0
                minDistance = 442
                for i in range(k):
                    newDistance = distance(pixelarray[x,y],centroids[i])
                    if newDistance<minDistance:
                        minDistance = newDistance
                        c_toset = i
                r_toset = round(centroids[c_toset][0])
                g_toset = round(centroids[c_toset][1])
                b_toset = round(centroids[c_toset][2])
                pixelarray[x,y] = (r_toset,g_toset,b_toset)

    #save new image
    print("Created new image " + picnum + '\n')
    im.save("image" + picnum +"_new.jpg")


def main():
    for image in range(1,4):
        colors = input("How many colors for image " + str(image) + '\n')
        runner(int(colors),str(image))
    print("Done: View created images in files")

main()
input()
