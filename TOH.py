def tower_of_hanoi(n, from_disk, to_disk, aux_disk):
    if n == 1:
        print("Move disk 1 from " + from_disk + " to " + to_disk)
        return
    tower_of_hanoi(n - 1, from_disk, aux_disk, to_disk)
    print("Move disk", n, "from", from_disk, "to", to_disk)
    tower_of_hanoi(n - 1, aux_disk, to_disk, from_disk)


num = int(input("Enter the number of disks: "))
tower_of_hanoi(num, 'A', 'C', 'B')
