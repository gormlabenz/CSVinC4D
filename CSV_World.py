import c4d
from c4d import gui
import csv

#Postions
lat = []
lon = []
vec = []



#Adjustmenst
radiusscale = 1000
abstand = 40
yabstand = 20
mapscl = 40

#Names
countries = []

def add_null(nullname):
    null = c4d.BaseObject(c4d.Onull)
    null.SetName(nullname)
    doc.InsertObject(null)
    doc.AddUndo(c4d.UNDOTYPE_NEW, null)
    c4d.EventAdd()


def add_sphere(xpos, zpos, sphereparent, spherename):
    #Create obj in memory
    obj = c4d.BaseObject(c4d.Osphere)


    #Set obj names
    obj.SetName(spherename)


    #Set disc_parameter
    obj[c4d.PRIM_SPHERE_RAD] = 10
    obj[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z] = zpos
    obj[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_X] = xpos

    obj.InsertUnder(sphereparent)
    doc.AddUndo(c4d.UNDOTYPE_NEW, obj)
    c4d.EventAdd()

def add_spline(row_count, points, splinename, parent):
    #Create splie in memory
    #spline = c4d.BaseObject(c4d.Ospline)
    spline = c4d.SplineObject(row_count, c4d.SPLINETYPE_BEZIER)


    #Set obj names
    spline.SetName("{}".format(splinename))
    #spline.SetName("{} Spline Year {}".format(str(num).zfill(2), name))

    #insert disc into the doc
    doc.InsertObject(spline)
    doc.AddUndo(c4d.UNDOTYPE_NEW, spline)

    spline.SetAllPoints(points)
    spline.InsertUnder(parent)
    c4d.EventAdd()

def add_lathe(namelathe, latpos, latheparent):
    lathe  = c4d.BaseObject(c4d.Olathe)

    lathe.SetPhong(1, 1, 89)
    lathe.SetName("{}".format(namelathe))

    #lathe[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_X] = latx
    #lathe[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Y] = laty
    #lathe[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z] = latz
    lathe.SetRelPos(latpos)
    #lathe[c4d.LATHEOBJECT_ROTATE] = 360
    #lathe[c4d.LATHEOBJECT_MOVE] = -100
    #lathe[c4d.LATHEOBJECT_SCALE] = 12
    #lathe[c4d.LATHEOBJECT_SUB] = 64
    #insert loft into the doc
    lathe.InsertUnder(latheparent)

    doc.AddUndo(c4d.UNDOTYPE_NEW, lathe)

    c4d.EventAdd()


def main():


    path2 = #insert here data 2
    doc.StartUndo()


    #add nulls
    add_null("Countrie Spheres")
    add_null("CO2")

    with open(path2, 'rb') as latlong:
        readed = csv.DictReader(latlong, delimiter=',')

        pointcounter = 0
        for i, row in enumerate(readed):
            try:

                countrienames = str(row["name"])
                countries.append(countrienames)

                lonp = float(row["longitude"])*mapscl
                latp = float(row["latitude"])*mapscl
                null = 0

                vecp = c4d.Vector(lonp, null, latp)
                vec.append(vecp)

                #add sphere
                sphereparent = doc.SearchObject("Countrie Spheres")
                add_sphere(lonp, latp, sphereparent, countrienames)

                #add lathe
                latheparent = doc.SearchObject("CO2")
                add_lathe(countrienames, vecp, latheparent)
                pointcounter = pointcounter +1


            except:
                #print "Error while reading - {}".format(row)
                continue

    print vec
    print pointcounter

    path = #insert here CountriesLatLong

    doc.StartUndo()

    for x in countries:
        points = []
        abzug= 0


        with open(path, 'rb') as csv_file:
            readed = csv.DictReader(csv_file, delimiter=';')

            for i, row in enumerate(readed):
                try:

                    radius = float(row[x]) / radiusscale
                    radiussmall = radius / radiusscale

                    #ypos = (i) * yabstand

                    if radius == 0:
                        ypos = ypos
                        abzug = abzug +1
                    else:
                        ypos = (i-abzug) * yabstand

                    #Make Postion String for Loft
                    point = c4d.Vector(0, ypos, radiussmall)
                    points.append(point)

                except:
                    #print "Error while reading - {}".format(row)
                    continue



        #make last point of spline closed
        point = c4d.Vector(0, ypos, 0)
        points.append(point)

        parent = doc.SearchObject(x)
        add_spline(len(points), points, x, parent)
        print "Abzug:" + str(abzug)

    print points
    c4d.EventAdd()
    doc.EndUndo()


# Execute main()
if __name__=='__main__':
    main()
