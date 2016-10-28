from os import statvfs

statfs =  statvfs("/")

print statfs.f_bavail * statfs.f_frsize
