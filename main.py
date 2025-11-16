from storage import load_data, save_data
import recipes
import planner
import shopping


def main():
    recipes_list, weekplan = load_data()

    while True:
        print("\n------------------------------")
        print(" MenuMaster (Rezeptplaner)")
        print("------------------------------")
        print("1) Rezepte anzeigen")
        print("2) Wochenplan anzeigen")
        print("3) Wochenplan neu (manuell)")
        print("4) Wochenplan neu (zufällig)")
        print("5) Einkaufsliste generieren")
        print("0) Beenden")

        choice = input("Auswahl: ").strip()

        if choice == "1":
            recipes_list = recipes.list_recipes(recipes_list)
        elif choice == "2":
            planner.show_weekplan(weekplan)
            input("Weiter mit Enter...")
        elif choice == "3":
            weekplan = planner.create_manual_weekplan(recipes_list)
            input("Weiter mit Enter...")
        elif choice == "4":
            weekplan = planner.create_random_weekplan(recipes_list)
            input("Weiter mit Enter...")
        elif choice == "5":
            shopping.generate_shopping_list(recipes_list, weekplan)
            input("Weiter mit Enter...")
        elif choice == "0":
            save_data(recipes_list, weekplan)
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl.")

    
if __name__ == "__main__":
    main()
