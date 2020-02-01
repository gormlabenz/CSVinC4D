import c4d
from c4d import gui
import csv

def add_spline(row_count, points):

    spline = c4d.SplineObject(row_count, c4d.SPLINETYPE_BEZIER)

    doc.InsertObject(spline)
    doc.AddUndo(c4d.UNDOTYPE_NEW, spline)

    spline.SetAllPoints(points)

    c4d.EventAdd()

def main():
    path = #insert here data.csv
    points = []
    counter = 0
    doc.StartUndo()
    with open(path, 'rb') as csv_file:
        readed = csv.DictReader(csv_file, delimiter=',')

        for i, row in enumerate(readed):


            entity = str(row["Entity"])
            year = float(row["Year"])
            emission = float(row["Annual CO₂ emissions (tonnes )"])            

            if year == 2017:
                
                counter = counter +1
                xpos = emission / 13317399
                ypos = i + counter
                point = c4d.Vector(xpos, ypos, 0)
                points.append(point)


    add_spline(len(points), points)
    print(points)
    print counter
    c4d.EventAdd()

 # Execute main()
if __name__=='__main__':
    main()
