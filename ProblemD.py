password = int(input())
firewall = int(input())

if password == firewall:
    print("PassBird has the correct number of passwords.")
elif password > firewall:
    print("Cora Programadora views her photo library with " +
          str(password - firewall) + " extra passwords in PassBird.")
elif password < firewall:
    print("Cora Programadora needs " + str(firewall - password) +
          " more passwords in PassBird to view her photo library.")
