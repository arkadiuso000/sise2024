
import matplotlib.pyplot as plt
import pandas as pan

data = pan.read_csv("all_stats.txt", sep=" ",encoding='utf-16le',
                   names=["glebokoscPoczatkowa", "nrPlanszy", "strategia", "parametr", "dlugoscRzowiazania",
                          "odwiedzone", "przetworzone", "maxGlebokosc", "czasProcesu"])

# print(data)
data_astr = data.loc[data['strategia'] == "astr"]
astr_hamm = data_astr.loc[data_astr['parametr'] =="hamm"]
astr_manh = data_astr.loc[data_astr['parametr'] =="manh"]
data_dfs = data.loc[data['strategia'] == "dfs"]
data_bfs = data.loc[data['strategia'] == "bfs"]
#print(astr_manh)

# data_astr_hamm_odwiedzone = astr_hamm[['glebokoscPoczatkowa', 'odwiedzone']]
# data_astr_manh_odwiedzone = astr_manh[['glebokoscPoczatkowa', 'odwiedzone']]
# #print(data_astr_hamm_odwiedzone)
# data_astr_hamm_odwiedzone_1 = data_astr_hamm_odwiedzone.loc[data_astr_hamm_odwiedzone['glebokoscPoczatkowa'] == 1]
# print(data_astr_hamm_odwiedzone_1)
# srednia = data_astr_hamm_odwiedzone_1['odwiedzone'].mean()
# print(srednia)


def wykres_astr(filename, Xtitle, Ytitle, Mtitle, kryterium, astr_hamm, astr_manh):
    box = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    index = [1, 2, 3, 4, 5, 6, 7]

    data_astr_hamm = astr_hamm[['glebokoscPoczatkowa', kryterium]]
    data_astr_manh = astr_manh[['glebokoscPoczatkowa', kryterium]]

    for i in range(7):
        tmp = data_astr_hamm.loc[data_astr_hamm['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[0][i] = srednia
        tmp = data_astr_manh.loc[data_astr_manh['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[1][i] = srednia

    bar_width = 0.3  # Szerokość słupków
    index_hamm = [i - bar_width / 2 for i in index]
    index_manh = [i + bar_width / 2 for i in index]

    plt.bar(index_hamm, box[0], color='#1f77b4', width=bar_width, label='Hamming')
    plt.bar(index_manh, box[1], color='#ff7f0e', width=bar_width, label='Manhattan')

    #plt.xlabel(Xtitle)
    #plt.ylabel(Ytitle)
    plt.title(Mtitle)
    plt.legend()
    plt.savefig(filename)
    plt.show()


def wykres_bfs(filename, Xtitle, Ytitle, Mtitle, kryterium, data_bfs):
    box = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    index = [1, 2, 3, 4, 5, 6, 7]

    bfs_drlu = data_bfs.loc[data_bfs['parametr'] == "drlu"]
    bfs_drul = data_bfs.loc[data_bfs['parametr'] == "drul"]
    bfs_ludr = data_bfs.loc[data_bfs['parametr'] == "ludr"]
    bfs_lurd = data_bfs.loc[data_bfs['parametr'] == "lurd"]
    bfs_rdlu = data_bfs.loc[data_bfs['parametr'] == "rdlu"]
    bfs_rdul = data_bfs.loc[data_bfs['parametr'] == "rdul"]
    bfs_uldr = data_bfs.loc[data_bfs['parametr'] == "uldr"]
    bfs_ulrd = data_bfs.loc[data_bfs['parametr'] == "ulrd"]
    data_bfs_drlu = bfs_drlu[['glebokoscPoczatkowa', kryterium]]
    data_bfs_drul = bfs_drul[['glebokoscPoczatkowa', kryterium]]
    data_bfs_ludr = bfs_ludr[['glebokoscPoczatkowa', kryterium]]
    data_bfs_lurd = bfs_lurd[['glebokoscPoczatkowa', kryterium]]
    data_bfs_rdlu = bfs_rdlu[['glebokoscPoczatkowa', kryterium]]
    data_bfs_rdul = bfs_rdul[['glebokoscPoczatkowa', kryterium]]
    data_bfs_uldr = bfs_uldr[['glebokoscPoczatkowa', kryterium]]
    data_bfs_ulrd = bfs_ulrd[['glebokoscPoczatkowa', kryterium]]

    for i in range(7):
        tmp = data_bfs_rdul.loc[data_bfs_rdul['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[0][i] = srednia
        tmp = data_bfs_rdlu.loc[data_bfs_rdlu['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[1][i] = srednia
        tmp = data_bfs_drul.loc[data_bfs_drul['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[2][i] = srednia
        tmp = data_bfs_drlu.loc[data_bfs_drlu['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[3][i] = srednia
        tmp = data_bfs_ludr.loc[data_bfs_ludr['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[4][i] = srednia
        tmp = data_bfs_lurd.loc[data_bfs_lurd['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[5][i] = srednia
        tmp = data_bfs_uldr.loc[data_bfs_uldr['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[6][i] = srednia
        tmp = data_bfs_ulrd.loc[data_bfs_ulrd['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[7][i] = srednia

    bar_width = 0.08  # Szerokość słupków
    index_rdul = [i - bar_width * 7 / 2 for i in index]
    index_rdlu = [i - bar_width * 5 / 2 for i in index]
    index_drul = [i - bar_width * 3 / 2 for i in index]
    index_drlu = [i - bar_width / 2 for i in index]
    index_ludr = [i + bar_width / 2 for i in index]
    index_lurd = [i + bar_width * 3 / 2 for i in index]
    index_uldr = [i + bar_width * 5 / 2 for i in index]
    index_ulrd = [i + bar_width * 7 / 2 for i in index]

    plt.bar(index_rdul, box[0], color='#e377c2', width=bar_width, label='RDUL')
    plt.bar(index_rdlu, box[1], color='#2ca02c', width=bar_width, label='RDLU')
    plt.bar(index_drul, box[2], color='#ff7f0e', width=bar_width, label='DRUL')
    plt.bar(index_drlu, box[3], color='#d62728', width=bar_width, label='DRLU')
    plt.bar(index_ludr, box[4], color='#9467bd', width=bar_width, label='LUDR')
    plt.bar(index_lurd, box[5], color='#1f77b4', width=bar_width, label='LURD')
    plt.bar(index_uldr, box[6], color='#8c564b', width=bar_width, label='ULDR')
    plt.bar(index_ulrd, box[7], color='#7f7f7f', width=bar_width, label='ULRD')

    plt.xlabel(Xtitle)
    plt.ylabel(Ytitle)
    plt.title(Mtitle)
    plt.legend()
    plt.savefig(filename)
    plt.show()

def wykres_dfs(filename, Xtitle, Ytitle, Mtitle, kryterium, data_bfs):
    box = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    index = [1, 2, 3, 4, 5, 6, 7]

    bfs_drlu = data_bfs.loc[data_bfs['parametr'] == "drlu"]
    bfs_drul = data_bfs.loc[data_bfs['parametr'] == "drul"]
    bfs_ludr = data_bfs.loc[data_bfs['parametr'] == "ludr"]
    bfs_lurd = data_bfs.loc[data_bfs['parametr'] == "lurd"]
    bfs_rdlu = data_bfs.loc[data_bfs['parametr'] == "rdlu"]
    bfs_rdul = data_bfs.loc[data_bfs['parametr'] == "rdul"]
    bfs_uldr = data_bfs.loc[data_bfs['parametr'] == "uldr"]
    bfs_ulrd = data_bfs.loc[data_bfs['parametr'] == "ulrd"]
    data_bfs_drlu = bfs_drlu[['glebokoscPoczatkowa', kryterium]]
    data_bfs_drul = bfs_drul[['glebokoscPoczatkowa', kryterium]]
    data_bfs_ludr = bfs_ludr[['glebokoscPoczatkowa', kryterium]]
    data_bfs_lurd = bfs_lurd[['glebokoscPoczatkowa', kryterium]]
    data_bfs_rdlu = bfs_rdlu[['glebokoscPoczatkowa', kryterium]]
    data_bfs_rdul = bfs_rdul[['glebokoscPoczatkowa', kryterium]]
    data_bfs_uldr = bfs_uldr[['glebokoscPoczatkowa', kryterium]]
    data_bfs_ulrd = bfs_ulrd[['glebokoscPoczatkowa', kryterium]]

    for i in range(7):
        tmp = data_bfs_rdul.loc[data_bfs_rdul['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[0][i] = srednia
        tmp = data_bfs_rdlu.loc[data_bfs_rdlu['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[1][i] = srednia
        tmp = data_bfs_drul.loc[data_bfs_drul['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[2][i] = srednia
        tmp = data_bfs_drlu.loc[data_bfs_drlu['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[3][i] = srednia
        tmp = data_bfs_ludr.loc[data_bfs_ludr['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[4][i] = srednia
        tmp = data_bfs_lurd.loc[data_bfs_lurd['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[5][i] = srednia
        tmp = data_bfs_uldr.loc[data_bfs_uldr['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[6][i] = srednia
        tmp = data_bfs_ulrd.loc[data_bfs_ulrd['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[7][i] = srednia

    bar_width = 0.08  # Szerokość słupków
    index_rdul = [i - bar_width * 7 / 2 for i in index]
    index_rdlu = [i - bar_width * 5 / 2 for i in index]
    index_drul = [i - bar_width * 3 / 2 for i in index]
    index_drlu = [i - bar_width / 2 for i in index]
    index_ludr = [i + bar_width / 2 for i in index]
    index_lurd = [i + bar_width * 3 / 2 for i in index]
    index_uldr = [i + bar_width * 5 / 2 for i in index]
    index_ulrd = [i + bar_width * 7 / 2 for i in index]

    plt.bar(index_rdul, box[0], color='#e377c2', width=bar_width, label='RDUL')
    plt.bar(index_rdlu, box[1], color='#2ca02c', width=bar_width, label='RDLU')
    plt.bar(index_drul, box[2], color='#ff7f0e', width=bar_width, label='DRUL')
    plt.bar(index_drlu, box[3], color='#d62728', width=bar_width, label='DRLU')
    plt.bar(index_ludr, box[4], color='#9467bd', width=bar_width, label='LUDR')
    plt.bar(index_lurd, box[5], color='#1f77b4', width=bar_width, label='LURD')
    plt.bar(index_uldr, box[6], color='#8c564b', width=bar_width, label='ULDR')
    plt.bar(index_ulrd, box[7], color='#7f7f7f', width=bar_width, label='ULRD')

    plt.xlabel(Xtitle)
    #plt.ylabel(Ytitle)
    plt.title(Mtitle)
    #plt.yscale("log")
    plt.savefig(filename)
    plt.show()

def wykres_razem(filename, Xtitle, Ytitle, Mtitle, kryterium, data_astr, data_bfs, data_dfs):
    box = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]
    index = [1, 2, 3, 4, 5, 6, 7]

    astr = data_astr[['glebokoscPoczatkowa', kryterium]]
    bfs = data_bfs[['glebokoscPoczatkowa', kryterium]]
    dfs = data_dfs[['glebokoscPoczatkowa', kryterium]]

    for i in range(7):
        tmp = bfs.loc[bfs['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[0][i] = srednia
        tmp = dfs.loc[dfs['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[1][i] = srednia
        tmp = astr.loc[astr['glebokoscPoczatkowa'] == i + 1]
        srednia = tmp[kryterium].mean()
        box[2][i] = srednia

    bar_width = 0.2  # Szerokość słupków
    index_bfs = [i - bar_width for i in index]
    index_dfs = [i for i in index]
    index_astr = [i + bar_width for i in index]

    plt.bar(index_bfs, box[0], color='#1f77b4', width=bar_width, label='BFS')
    plt.bar(index_dfs, box[1], color='#ff7f0e', width=bar_width, label='DFS')
    plt.bar(index_astr, box[2], color='#2ca02c', width=bar_width, label='A*')

    #plt.xlabel(Xtitle)
    plt.ylabel(Ytitle)
    plt.title(Mtitle)
    plt.legend()
    plt.yscale("log")
    plt.savefig(filename)
    plt.show()


#Długość rozwiązania
wykres_razem("1_Dlug_rozw_razem.png", 'Głębokość', 'Długość rozwiązania', 'Ogółem', 'dlugoscRzowiazania', data_astr, data_bfs, data_dfs)
wykres_astr("1_Dlug_rozw_astr.png", 'Głębokość', 'Długość rozwiązania', 'A*', 'dlugoscRzowiazania', astr_hamm, astr_manh)
wykres_bfs("1_Dlug_rozw_bfs.png", 'Głębokość', 'Długość rozwiązania', 'BFS', 'dlugoscRzowiazania', data_bfs)
wykres_dfs("1_Dlug_rozw_dfs.png", 'Głębokość', 'Długość rozwiązania', 'DFS', 'dlugoscRzowiazania', data_dfs)
#Odwiedzone stany
wykres_razem("2_Odw_stany_razem.png", 'Głębokość', 'Odwiedzone stany', 'Ogółem', 'odwiedzone', data_astr, data_bfs, data_dfs)
wykres_astr("2_Odw_stany_astr.png", 'Głębokość', 'Odwiedzone stany', 'A*', 'odwiedzone', astr_hamm, astr_manh)
wykres_bfs("2_Odw_stany_bfs.png", 'Głębokość', 'Odwiedzone stany', 'BFS', 'odwiedzone', data_bfs)
wykres_dfs("2_Odw_stany_dfs.png", 'Głębokość', 'Odwiedzone stany', 'DFS', 'odwiedzone', data_dfs)
#Przetworzone stany
wykres_razem("3_Przetw_stany_razem.png", 'Głębokość', 'Przetworzone stany', 'Ogółem', 'przetworzone', data_astr, data_bfs, data_dfs)
wykres_astr("3_Przetw_stany_astr.png", 'Głębokość', 'Przetworzone stany', 'A*', 'przetworzone', astr_hamm, astr_manh)
wykres_bfs("3_Przetw_stany_bfs.png", 'Głębokość', 'Przetworzone stany', 'BFS', 'przetworzone', data_bfs)
wykres_dfs("3_Przetw_stany_dfs.png", 'Głębokość', 'Przetworzone stany', 'DFS', 'przetworzone', data_dfs)
#Maksymalna głębokość
wykres_razem("4_Maks_gleb_razem.png", 'Głębokość', 'Maksymalna głębokość', 'Ogółem', 'maxGlebokosc', data_astr, data_bfs, data_dfs)
wykres_astr("4_Maks_gleb_astr.png", 'Głębokość', 'Maksymalna głębokość', 'A*', 'maxGlebokosc', astr_hamm, astr_manh)
wykres_bfs("4_Maks_gleb_bfs.png", 'Głębokość', 'Maksymalna głębokość', 'BFS', 'maxGlebokosc', data_bfs)
wykres_dfs("4_Maks_gleb_dfs.png", 'Głębokość', 'Maksymalna głębokość', 'DFS', 'maxGlebokosc', data_dfs)
#Czas
wykres_razem("5_Czas_razem.png", 'Głębokość', 'Czas [s]', 'Ogółem', 'czasProcesu', data_astr, data_bfs, data_dfs)
wykres_astr("5_Czas_astr.png", 'Głębokość', 'Czas [s]', 'A*', 'czasProcesu', astr_hamm, astr_manh)
wykres_bfs("5_Czas_bfs.png", 'Głębokość', 'Czas [s]', 'BFS', 'czasProcesu', data_bfs)
wykres_dfs("5_Czas_dfs.png", 'Głębokość', 'Czas [s]', 'DFS', 'czasProcesu', data_dfs)
