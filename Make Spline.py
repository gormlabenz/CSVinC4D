import c4d
from c4d import gui
from c4d.modules import mograph as mo

rowncount = 30
objects = []

def getclones():
    py = doc.SearchObject("ArrayMaker")
    md = mo.GeGetMoData(py)
    if md is None: return 1.0
    cnt = md.GetCount()
    marr = md.GetArray(c4d.MODATA_MATRIX)
    clone = md.GetArray(c4d.MODATA_CLONE)
    for i in range(0,cnt):        
        objects.append(clone[i])

def add_spline(row_count, points):
    #Create splie in memory
    #spline = c4d.BaseObject(c4d.Ospline)
    spline = c4d.SplineObject(row_count, c4d.SPLINETYPE_BEZIER)


    #Set obj names
    #spline.SetName("{} Spline Year {}".format(str(num).zfill(2), name))

    #insert disc into the doc
    doc.InsertObject(spline)
    doc.AddUndo(c4d.UNDOTYPE_NEW, spline)

    spline.SetAllPoints(points)

    c4d.EventAdd()



def main():
    points = []
    getclones()


    for y in range(1,len(objects)):
        point = c4d.Vector(y, 5, 10)
        points.append(point)

    print(points)

    add_spline(y,points )


# Execute main()
if __name__=='__main__':
    main()