# Solve Tower of Hanoi for n disks.
#SOURCE->AUXILLARY->DESTINATION
# Explanation:
# Move top n-1 disks from source to auxiliary
# Move the largest disk (nth) from source to destination
# Move the n-1 disks from auxiliary to destination
def TOH(n,source,destination,auxillary):
    if n==1:
        print(f"move disk 1 from {source} to {destination}")
        return
    TOH(n-1,source,auxillary,destination)
    print(f"move disk {n} from {source} to {destination}")
    TOH(n-1,auxillary,destination,source)
TOH(2,'A','C','B')