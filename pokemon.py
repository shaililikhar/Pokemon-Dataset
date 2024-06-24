import csv

#1
with open("pokemonTrain.csv", "r") as f:
   readf = csv.reader(f)
   next(f)
   total_count = 0
   count_above_forty = 0
   for line in readf:
        level = float(line[2])
        if line[4] == 'fire':
            total_count += 1
            if level >= 40:
                count_above_forty += 1
    
    
percent = round(float(count_above_forty / total_count) * 100)

f = open('pokemon1.txt', 'w+')
f.write(f'Percentage of fire type pokemon at or above level 40 = {percent}')


#2
result = []
with open("pokemonTrain.csv", "r") as f:
    weakness_to_type = {}
    readf = csv.reader(f)
    heading = next(readf)
    result.append(heading)
    for line in readf:
        result.append(line)
        type = line[4]
        if type != "NaN":
            weakness = line[5]
            if weakness not in weakness_to_type:
                weakness_to_type[weakness] = {type:1}
            else:
                if weakness not in weakness_to_type[weakness]:
                    weakness_to_type[weakness][type] = 1
                else:
                    weakness_to_type[weakness][type] += 1
    for weakness in weakness_to_type:
        type_dict = weakness_to_type[weakness]
        type_list = [(k, v) for k, v in type_dict.items()]
        type_list.sort()
        type_list.sort(key=lambda x: x[1], reverse=True)
        weakness_to_type[weakness] = type_list[0][0]
    for i in range(len(result)):
        if result[i][4] == 'NaN':
            result[i][4] = weakness_to_type[result[i][5]]

#3
atkOver40_total = 0
atkUnder40_total = 0
defOver40_total = 0
defUnder40_total = 0
hpOver40_total = 0
hpUnder40_total = 0
atkOver40_count = 0
atkUnder40_count = 0
defOver40_count = 0
defUnder40_count = 0
hpOver40_count = 0
hpUnder40_count = 0

with open("pokemonTrain.csv", "r") as f:
   readf = csv.reader(f)
   next(f)
   for line in readf:
        if line[6] == 'NaN':
            continue
        else:
            if float(line[2]) > 40:
                atkOver40_total += float(line[6])
                atkOver40_count += 1
            else:
                atkUnder40_total += float(line[6])
                atkUnder40_count += 1

        if line[7] == 'NaN':
            continue
        else:
            if float(line[2]) > 40:
                defOver40_total += float(line[7])
                defOver40_count += 1
            else:
                defUnder40_total += float(line[7])
                defUnder40_count += 1

        if line[8] == 'NaN':
            continue
        else:
            if float(line[2]) > 40:
                hpOver40_total += float(line[8])
                hpOver40_count += 1
            else:
                hpUnder40_total += float(line[8])
                hpUnder40_count += 1



atkOver40_average = round(float(atkOver40_total / atkOver40_count),1)
atkUnder40_average = round(float(atkUnder40_total / atkUnder40_count),1)
defOver40_average = round(float(defOver40_total / defOver40_count),1)
defUnder40_average = round(float(defUnder40_total / defUnder40_count),1)
hpOver40_average = round(float(hpOver40_total / hpOver40_count),1)
hpUnder40_average = round(float(hpUnder40_total / hpUnder40_count),1)

for i in range(len(result)):
    if result[i][6] == 'NaN':
        if float(result[i][2]) > 40:
            result[i][6] = atkOver40_average
        else:
            result[i][6] = atkUnder40_average
    if result[i][7] == 'NaN':
        if float(result[i][2]) > 40:
            result[i][7] = defOver40_average
        else:
            result[i][7] = defUnder40_average
    if result[i][8] == 'NaN':
        if float(result[i][2]) > 40:
            result[i][8] = hpOver40_average
        else:
            result[i][8] = hpUnder40_average
            
with open('pokemonResult.csv', 'w') as out:
    csv_writer = csv.writer(out)
    for i in range(len(result)):
        csv_writer.writerow(result[i])



#4
dictionary = {}
with open("pokemonResult.csv", "r") as f:
    readf = csv.reader(f)
    next(f)
    for line in readf:
        if line[4] == 'type':
            continue
        if line[4] not in dictionary:
            dictionary[line[4]] = [line[3]]
        else:
            if line[3] not in dictionary[line[4]]:
                dictionary[line[4]].append(line[3])
                dictionary[line[4]].sort()
    
sortedDict = sorted(dictionary.items())
f = open('pokemon4.txt', 'w+')
f.write('Pokemon type to personality mapping:\n')
for type in sortedDict:
    str = type[0]+':'
    for i in range(len(type[1])):
        if(i == len(type[1]) - 1):
            str += type[1][i]
        else:
            str += type[1][i]+', '
    f.write(str+'\n')
   
#5
total = 0
count = 0
with open ('pokemonResult.csv', 'r') as file:
    reader = csv.DictReader(file)

    for line in reader:
        if float(line['stage']) > 2:
            total += float(line['hp'])
            count += 1

    avg = round(float(total / count))

f = open('pokemon5.txt', 'w+')
f.write(f'Average hit point for pokemon of stage 3.0 = {avg}')