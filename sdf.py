#!/usr/bin/env python
# coding: utf-8

__all__ = ['write_sdf',
         'atom_num',
         'source_name',
        'mol_weight']


def write_sdf(filename):
    with open(filename) as f:
        dat = f.readlines()
        data = []
        count = 1
        for line in dat:
            if line.startswith('$$$$'):
                data.append(line)
                mole = ''.join(data)
                mol = open("./writen_sdf_files/mol_%s.sdf" % str(count), "w")
                mol.write(mole)
                mol.close()
                count += 1
                data = []
                continue
            else:
                data.append(line)
    return print("The total molecule : %s" %str(count-1))

def _get_value(filename):
    with open(filename) as f:
        dat = f.readlines()
        mole = ''.join(dat)
        return dat

def atom_num(filename):
    dat = _get_value(filename)
    atom = dat[3].split()
    print("total atom number : {}".format(atom[0]))


def source_name(filename):
    dat = _get_value(filename)
    ss = "Source_ChemicalName"
    for i, line in enumerate(dat):
        if ss in line:
            name = ''.join(dat[i+1].split())
            print("Source Name is : {}".format(name))

def mol_weight(filename):
    dat = _get_value(filename)
    ss = "STRUCTURE_MolecularWeight"
    for i, line in enumerate(dat):
        if ss in line:
            name = ''.join(dat[i+1].split())
            print("Molecular weight is : {}".format(name))
	

write_sdf("./files/sample.sdf")


