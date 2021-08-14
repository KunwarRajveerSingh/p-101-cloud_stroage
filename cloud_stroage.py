import dropbox
class Transferdata:
    def __init__(self, accessToken) :
        self.accessToken = accessToken
    
    def uploadfile(self, filefrom ,fileto):
        dbx = dropbox.Dropbox(self.accessToken)
        f = open(filefrom,'rb')
        dbx.files_upload(f.read(),fileto)

def main():
    accessToken = 'sl.A2T2rpd36Tpon-Jk9ts8zVsncXmbg-Vi0fkgHS22qEMDYcP1nWE_u3u1Ytwfl5D2J_g6iXwVX-tWPjA_xUxHvfd7knieSTTCEYB20lgm0-_XeeNJb0tqfEHgVf_1kYMsyNBQj5PVnr_O'
    transferdata = Transferdata(accessToken)
    filefrom = input('enter the file path to transfer:-')
    fileto = input('enter the full path to upload to dropbox')
    transferdata.uploadfile(filefrom, fileto)
    print('file has been moved')

main()        
