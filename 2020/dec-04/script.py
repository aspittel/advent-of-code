with open('input.txt') as inp:
    passports = []
    passport = {}
    for line in inp:
        if line != "\n":
            line = line.rstrip().split(" ")
            line = [field.split(":") for field in line]
            for field in line:
                passport[field[0]] = field[1]
        else:
            passports.append(passport)
            passport = {}
    passports.append(passport)
    part_1_count = 0
    part_2_count = 0
    for passport in passports:
        if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport):
            part_1_count += 1
            if len(passport['byr']) == 4 and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002:
                if len(passport['iyr']) == 4 and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020:
                    if len(passport['eyr']) == 4 and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030:
                        if passport['hcl'][0] == "#" and passport['hcl'][1:].isalnum():
                            if passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                                if len(passport['pid']) == 9:
                                    if passport['hgt'][-2:] == "cm":
                                        if int(passport['hgt'][:-2]) >= 150 and int(passport['hgt'][:-2]) <= 193:
                                            part_2_count += 1
                                    elif passport['hgt'][-2:] == "in":
                                        if int(passport['hgt'][:-2]) >= 59 and int(passport['hgt'][:-2]) <= 76:
                                            part_2_count += 1

    print(part_1_count) 
    print(part_2_count)                
               
