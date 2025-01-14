# აქ ჩაწერე რამდენი ბავშვი დადის კვირში 1-ხელ 2-ჯერ 3-ჯერ და 4-ჯერ
kvirashi_1xel_raodenoba = 3
kvirashi_2jer_raodenoba = 5
kvirashi_3jer_raodenoba = 1
kvirashi_4jer_raodenoba = 0


kvirashi_1xel = kvirashi_1xel_raodenoba * 1
kvirashi_2jer = kvirashi_2jer_raodenoba * 2
kvirashi_3jer = kvirashi_3jer_raodenoba * 3
kvirashi_4jer = kvirashi_4jer_raodenoba * 4


razmelebis_raodenoba = kvirashi_1xel_raodenoba + kvirashi_2jer_raodenoba + kvirashi_3jer_raodenoba + kvirashi_4jer_raodenoba
print("razmelebis raodenoba = " + str(razmelebis_raodenoba))


speed_count = ((kvirashi_1xel_raodenoba) + (kvirashi_2jer_raodenoba * 2) + (kvirashi_3jer_raodenoba * 3) + (kvirashi_4jer_raodenoba * 4))
print("razmelebis speedebis jami = " + str(speed_count))

#საბოლოო ბარათები
green_card = 0
baratebis_saboloo_procenti = 0 #%

# აქ თვეში 2 შემოწმების და მინილიდერების ჯარიმები
jarima_1 = 0
jarima_2 = 0
miniliderebis_jarimebi = 0

#დამატებითი შემოსავლები
asistentobis_saboloo_xelfasi = 0
github_kontroliori = 0
shtamos_xelpasis_procenti = 20 #მიახლოებით. ჯერ არ მაქ დათვლილი
gamblihg_procenti = 0
#ხარჯები
sandros_procenti = 0 #არაფერი არ ჩავწერო
miniliderebis_xelfasi = 0

if speed_count <= 20: 
    wage_per_speed = 6.75
    razmis_xelpasi = ((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) + (kvirashi_4jer / 4 * 3.33 * wage_per_speed))
    print("razmis xelpasi = " + str(razmis_xelpasi))
    razmis_saboloo_xelpasi = razmis_xelpasi - (razmis_xelpasi / 100 * baratebis_saboloo_procenti) + (green_card * 5) - jarima_1 - jarima_2 - miniliderebis_jarimebi
    sandros_procenti = (razmis_saboloo_xelpasi / 10)
    print("saboloo xelpasi rac unda chamericxos = " + str(razmis_saboloo_xelpasi + github_kontroliori + gamblihg_procenti))
    print("saboloo xelpasi = " + str(razmis_saboloo_xelpasi + asistentobis_saboloo_xelfasi + github_kontroliori + shtamos_xelpasis_procenti + gamblihg_procenti - sandros_procenti - miniliderebis_xelfasi))
elif speed_count <= 25: 
    wage_per_speed = 7
    razmis_xelpasi = ((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) + (kvirashi_4jer / 4 * 3.33 * wage_per_speed))
    print("razmis xelpasi = " + str(razmis_xelpasi))
    razmis_saboloo_xelpasi = razmis_xelpasi - (razmis_xelpasi / 100 * baratebis_saboloo_procenti) + (green_card * 5) - jarima_1 - jarima_2 - miniliderebis_jarimebi
    sandros_procenti = (razmis_saboloo_xelpasi / 10)
    print("saboloo xelpasi rac unda chamericxos = " + str(razmis_saboloo_xelpasi + github_kontroliori + gamblihg_procenti))
    print("saboloo xelpasi = " + str(razmis_saboloo_xelpasi + asistentobis_saboloo_xelfasi + github_kontroliori + shtamos_xelpasis_procenti + gamblihg_procenti - sandros_procenti - miniliderebis_xelfasi))
elif speed_count <= 30: 
    wage_per_speed = 7.25
    razmis_xelpasi = ((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) + (kvirashi_4jer / 4 * 3.33 * wage_per_speed))
    print("razmis xelpasi = " + str(razmis_xelpasi))
    razmis_saboloo_xelpasi = razmis_xelpasi - (razmis_xelpasi / 100 * baratebis_saboloo_procenti) + (green_card * 5) - jarima_1 - jarima_2 - miniliderebis_jarimebi
    sandros_procenti = (razmis_saboloo_xelpasi / 10)
    print("saboloo xelpasi rac unda chamericxos = " + str(razmis_saboloo_xelpasi + github_kontroliori + gamblihg_procenti))
    print("saboloo xelpasi = " + str(razmis_saboloo_xelpasi + asistentobis_saboloo_xelfasi + github_kontroliori + shtamos_xelpasis_procenti + gamblihg_procenti - sandros_procenti - miniliderebis_xelfasi))
elif speed_count <= 35: 
    wage_per_speed = 7.5
    razmis_xelpasi = ((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) + (kvirashi_4jer / 4 * 3.33 * wage_per_speed))
    print("razmis xelpasi = " + str(razmis_xelpasi))
    razmis_saboloo_xelpasi = razmis_xelpasi - (razmis_xelpasi / 100 * baratebis_saboloo_procenti) + (green_card * 5) - jarima_1 - jarima_2 - miniliderebis_jarimebi
    sandros_procenti = (razmis_saboloo_xelpasi / 10)
    print("saboloo xelpasi rac unda chamericxos = " + str(razmis_saboloo_xelpasi + github_kontroliori + gamblihg_procenti))
    print("saboloo xelpasi = " + str(razmis_saboloo_xelpasi + asistentobis_saboloo_xelfasi + github_kontroliori + shtamos_xelpasis_procenti + gamblihg_procenti - sandros_procenti - miniliderebis_xelfasi))
elif speed_count <= 40: 
    wage_per_speed = 7.75
    razmis_xelpasi = ((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) + (kvirashi_4jer / 4 * 3.33 * wage_per_speed))
    print("razmis xelpasi = " + str(razmis_xelpasi))
    razmis_saboloo_xelpasi = razmis_xelpasi - (razmis_xelpasi / 100 * baratebis_saboloo_procenti) + (green_card * 5) - jarima_1 - jarima_2 - miniliderebis_jarimebi
    sandros_procenti = (razmis_saboloo_xelpasi / 10)
    print("saboloo xelpasi rac unda chamericxos = " + str(razmis_saboloo_xelpasi + github_kontroliori + gamblihg_procenti))
    print("saboloo xelpasi = " + str(razmis_saboloo_xelpasi + asistentobis_saboloo_xelfasi + github_kontroliori + shtamos_xelpasis_procenti + gamblihg_procenti - sandros_procenti - miniliderebis_xelfasi))
elif speed_count <= 45: 
    wage_per_speed = 8
    razmis_xelpasi = ((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) + (kvirashi_4jer / 4 * 3.33 * wage_per_speed))
    print("razmis xelpasi = " + str(razmis_xelpasi))
    razmis_saboloo_xelpasi = razmis_xelpasi - (razmis_xelpasi / 100 * baratebis_saboloo_procenti) + (green_card * 5) - jarima_1 - jarima_2 - miniliderebis_jarimebi
    sandros_procenti = (razmis_saboloo_xelpasi / 10)
    print("saboloo xelpasi rac unda chamericxos = " + str(razmis_saboloo_xelpasi + github_kontroliori + gamblihg_procenti))
    print("saboloo xelpasi = " + str(razmis_saboloo_xelpasi + asistentobis_saboloo_xelfasi + github_kontroliori + shtamos_xelpasis_procenti + gamblihg_procenti - sandros_procenti - miniliderebis_xelfasi))
elif speed_count <= 50: 
    wage_per_speed = 8.25
    razmis_xelpasi = ((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) + (kvirashi_4jer / 4 * 3.33 * wage_per_speed))
    print("razmis xelpasi = " + str(razmis_xelpasi))
    razmis_saboloo_xelpasi = razmis_xelpasi - (razmis_xelpasi / 100 * baratebis_saboloo_procenti) + (green_card * 5) - jarima_1 - jarima_2 - miniliderebis_jarimebi
    sandros_procenti = (razmis_saboloo_xelpasi / 10)
    print("saboloo xelpasi rac unda chamericxos = " + str(razmis_saboloo_xelpasi + github_kontroliori + gamblihg_procenti))
    print("saboloo xelpasi = " + str(razmis_saboloo_xelpasi + asistentobis_saboloo_xelfasi + github_kontroliori + shtamos_xelpasis_procenti + gamblihg_procenti - sandros_procenti - miniliderebis_xelfasi))
elif speed_count <= 55: 
    wage_per_speed = 8.5
    razmis_xelpasi = ((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) + (kvirashi_4jer / 4 * 3.33 * wage_per_speed))
    print("razmis xelpasi = " + str(razmis_xelpasi))
    razmis_saboloo_xelpasi = razmis_xelpasi - (razmis_xelpasi / 100 * baratebis_saboloo_procenti) + (green_card * 5) - jarima_1 - jarima_2 - miniliderebis_jarimebi
    sandros_procenti = (razmis_saboloo_xelpasi / 10)
    print("saboloo xelpasi rac unda chamericxos = " + str(razmis_saboloo_xelpasi + github_kontroliori + gamblihg_procenti))
    print("saboloo xelpasi = " + str(razmis_saboloo_xelpasi + asistentobis_saboloo_xelfasi + github_kontroliori + shtamos_xelpasis_procenti + gamblihg_procenti - sandros_procenti - miniliderebis_xelfasi))
elif speed_count <= 60: 
    wage_per_speed = 8.75
    razmis_xelpasi = ((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) + (kvirashi_4jer / 4 * 3.33 * wage_per_speed))
    print("razmis xelpasi = " + str(razmis_xelpasi))
    razmis_saboloo_xelpasi = razmis_xelpasi - (razmis_xelpasi / 100 * baratebis_saboloo_procenti) + (green_card * 5) - jarima_1 - jarima_2 - miniliderebis_jarimebi
    sandros_procenti = (razmis_saboloo_xelpasi / 10)
    print("saboloo xelpasi rac unda chamericxos = " + str(razmis_saboloo_xelpasi + github_kontroliori + gamblihg_procenti))
    print("saboloo xelpasi = " + str(razmis_saboloo_xelpasi + asistentobis_saboloo_xelfasi + github_kontroliori + shtamos_xelpasis_procenti + gamblihg_procenti - sandros_procenti - miniliderebis_xelfasi))
elif speed_count <= 65: 
    wage_per_speed = 9
    razmis_xelpasi = ((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) + (kvirashi_4jer / 4 * 3.33 * wage_per_speed))
    print("razmis xelpasi = " + str(razmis_xelpasi))
    razmis_saboloo_xelpasi = razmis_xelpasi - (razmis_xelpasi / 100 * baratebis_saboloo_procenti) + (green_card * 5) - jarima_1 - jarima_2 - miniliderebis_jarimebi
    sandros_procenti = (razmis_saboloo_xelpasi / 10)
    print("saboloo xelpasi rac unda chamericxos = " + str(razmis_saboloo_xelpasi + github_kontroliori + gamblihg_procenti))
    print("saboloo xelpasi = " + str(razmis_saboloo_xelpasi + asistentobis_saboloo_xelfasi + github_kontroliori + shtamos_xelpasis_procenti + gamblihg_procenti - sandros_procenti - miniliderebis_xelfasi))
elif speed_count <= 70: 
    wage_per_speed = 9.25
    razmis_xelpasi = ((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) + (kvirashi_4jer / 4 * 3.33 * wage_per_speed))
    print("razmis xelpasi = " + str(razmis_xelpasi))
    razmis_saboloo_xelpasi = razmis_xelpasi - (razmis_xelpasi / 100 * baratebis_saboloo_procenti) + (green_card * 5) - jarima_1 - jarima_2 - miniliderebis_jarimebi
    sandros_procenti = (razmis_saboloo_xelpasi / 10)
    print("saboloo xelpasi rac unda chamericxos = " + str(razmis_saboloo_xelpasi + github_kontroliori + gamblihg_procenti))
    print("saboloo xelpasi = " + str(razmis_saboloo_xelpasi + asistentobis_saboloo_xelfasi + github_kontroliori + shtamos_xelpasis_procenti + gamblihg_procenti - sandros_procenti - miniliderebis_xelfasi))
elif speed_count <= 75: 
    wage_per_speed = 9.5
    razmis_xelpasi = ((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) + (kvirashi_4jer / 4 * 3.33 * wage_per_speed))
    print("razmis xelpasi = " + str(razmis_xelpasi))
    razmis_saboloo_xelpasi = razmis_xelpasi - (razmis_xelpasi / 100 * baratebis_saboloo_procenti) + (green_card * 5) - jarima_1 - jarima_2 - miniliderebis_jarimebi
    sandros_procenti = (razmis_saboloo_xelpasi / 10)
    print("saboloo xelpasi rac unda chamericxos = " + str(razmis_saboloo_xelpasi + github_kontroliori + gamblihg_procenti))
    print("saboloo xelpasi = " + str(razmis_saboloo_xelpasi + asistentobis_saboloo_xelfasi + github_kontroliori + shtamos_xelpasis_procenti + gamblihg_procenti - sandros_procenti - miniliderebis_xelfasi))
else: 
    wage_per_speed = 9.75
    razmis_xelpasi = ((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) + (kvirashi_4jer / 4 * 3.33 * wage_per_speed))
    print("razmis xelpasi = " + str(razmis_xelpasi))
    razmis_saboloo_xelpasi = razmis_xelpasi - (razmis_xelpasi / 100 * baratebis_saboloo_procenti) + (green_card * 5) - jarima_1 - jarima_2 - miniliderebis_jarimebi
    sandros_procenti = (razmis_saboloo_xelpasi / 10)
    print("saboloo xelpasi rac unda chamericxos = " + str(razmis_saboloo_xelpasi + github_kontroliori + gamblihg_procenti))
    print("saboloo xelpasi = " + str(razmis_saboloo_xelpasi + asistentobis_saboloo_xelfasi + github_kontroliori + shtamos_xelpasis_procenti + gamblihg_procenti - sandros_procenti - miniliderebis_xelfasi))

