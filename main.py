# Main menu

import triarblogic
import os.path
import time

nowFormat = "%Y-%m-%d %H:%M:%S"

stp_path = "structured_triangular_pairs.json"
usr_path = "uniswap_surface_rates.json"

if __name__ == '__main__':

    close = False

    while close is False:

        nowTime = time.strftime(nowFormat, time.localtime())

        if os.path.exists(stp_path):

            last_modified = os.path.getmtime(stp_path)
            last_stp_modified_time = time.strftime(nowFormat, time.localtime(last_modified))

        else:

            last_stp_modified_time = "N/A"

        if os.path.exists(usr_path):

            last_modified = os.path.getmtime(usr_path)
            last_usr_modified_time = time.strftime(nowFormat, time.localtime(last_modified))

        else:

            last_usr_modified_time = "N/A"

        print("\nMain Menu:\n")
        print("Current time:", nowTime, "\n")
        print("1. Get token pools.")
        print("2. Update structured pair list. Last time updated: ", last_stp_modified_time)
        print("3. Update uniswap surface rates. Last time updated: ", last_usr_modified_time)
        print("4. ...")
        print("5. ...")
        print("6. Exit.")

        opc = int(input("\nPick an option: "))

        if opc == 1:

            pools = triarblogic.retrieve_uniswap_info()["data"]["pools"]
            print("Tokens pool list has been updated\n")

        elif opc == 2:

            triarblogic.structure_triangular_pairs(pools)
            print("Pool list has been structured\n")

        elif opc == 3:

            min_rate = 5
            triarblogic.triangular_arb_surface_rate(min_rate)
            print("Uniswap surface rates has been generated\n")

        elif opc == 4:

            print("Opc4")

        elif opc == 5:

            print("Opc5")

        elif opc == 6:

            print("\nClosing program\n")
            close = True