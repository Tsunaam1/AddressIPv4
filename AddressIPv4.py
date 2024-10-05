class AddressIPv4:
    def __init__(self, address):
        self.address = address
        self.ls = list(self.address.split("."))

    def isValid(self):
        validStatus = False
        if len(self.ls) != 4:
            validStatus = False
        else:
            validStatus = True
        for x in self.ls:
            if int(x) < 0 or int(x) > 255:
                validStatus = False
        if validStatus == False:
            raise Exception("Tak to v žádném případě!")
        return validStatus
    
    def getString(self):
        #??? nepochopil jsem, k cemu je tahle funkce, ale dobre
        return self.address

    def getAsBinaryString(self):
        lsb_temp = []
        lsb = []
        self.lsbb = []
        lsb_result = ""

        def __decToBin():
            count = 0
            octcount = 0
            self.ls.reverse()
            for x in self.ls:
                # print(int(x))
                if int(x) ==  0:
                    # print("Lyup")
                    # print(octcount)
                    if octcount < 8:
                        # print("henshin")
                        while octcount < 8:
                            lsb_temp.append("0")
                            octcount += 1
                            # print("appended 0")
                while int(x) > 0:
                    if int(x) % 2 == 0:
                        lsb_temp.append("0")
                    else:
                        lsb_temp.append("1")
                    octcount += 1
                    x = int(x) // 2
                    # print(lsb_temp)
                # print("kookot", octcount)
                if octcount < 8:
                    # print(lsb_temp)
                    # print("henshin")
                    while octcount < 8:
                        lsb_temp.append("0")
                        octcount += 1
                        # print("appended 0")
                # print("afterall count", octcount)
                octcount = 0
                # print(lsb_temp, "afterapp")
            # print("lsb_temp", lsb_temp) 
            for x in lsb_temp:
                count += 1
                if count > 8:
                    count = 1
                    lsb.append(".")
                lsb.append(x)
            lsb.reverse()
            
        __decToBin()
        self.ls.reverse()
        lsb_temp.reverse()
        self.lsb_nodots = "".join(lsb_temp)
        self.lsb_nodots = int(self.lsb_nodots)
        lsb_result = "".join(lsb)
        # print(lsb)
        return lsb_result

    def getOctet(self, number=0):
        if number > 3:
            return "Ale notáák.."
        return self.ls[number]
    
    def getClass(self):
        firstoct = int(self.ls[0])
        if firstoct < 128:
            return "A"
        elif firstoct < 192:
            return "B"
        elif firstoct < 224:
            return "C"
        else:
            return "D"

    def getInt(self):
        result = 0
        result += int(self.getOctet()) * 256 ** 3
        result += int(self.getOctet(1)) * 256 ** 2
        result += int(self.getOctet(2)) * 256 ** 1
        result += int(self.getOctet(3)) * 256 ** 0
        return result

    def isPrivate(self):
        if (self.lsb_nodots >= 1010000000000000000000000000 and self.lsb_nodots <= 1010111111111111111111111111 or self.lsb_nodots >= 10101100000100000000000000000000 and self.lsb_nodots <= 10101100000111111111111111111111 or self.lsb_nodots >= 11000000101010000000000000000000 and self.lsb_nodots <= 11000000101010001111111111111111):
            return(True)
        else:
            return(False)

sd = AddressIPv4("192.168.10.1")
print(sd.isValid())
print(sd.getString())
print(sd.getAsBinaryString())
print(sd.getOctet(2))
print(sd.getClass())
print(sd.getInt())
print(sd.isPrivate())