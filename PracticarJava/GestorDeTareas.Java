import java.util.Scanner;

public class GestorDeTareas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int opcion;
        int totalPrioridad = 0;

        do {
            System.out.println("=== Gestor de Tareas. ===");
            System.out.println("1. Agregar tarea.");
            System.out.println("2. Ver tareas. (Pendientes)");
            System.out.println("3. Salir.");
            System.out.print("Selecciona una opcion: ");
            opcion = sc.nextInt();
            sc.nextLine(); // Limpiar

            switch (opcion) {
                case 1:
                    System.out.print("Nombre de la tarea: ");
                    String nombre = sc.nextLine();

                    System.out.print("Prioridad (1 a 5): ");
                    int prioridad = sc.nextInt();
                    sc.nextLine();

                    if (prioridad >= 1 && prioridad <= 5) {
                        totalPrioridad += prioridad; // Se acumula la prioridad
                        System.out.println("Tarea '" + nombre + "' con prioridad " + prioridad + " agregada");
                        System.out.println("Total acumulado de prioridades: " + totalPrioridad);
                    }else{
                        System.out.println("Prioridad no valida.");
                    }
                    break;
                case 2:
                    System.out.println("Funcionalidad aun no implementada.");
                    break;
                case 3:
                    System.out.println("Hasta luego!");
                    break;
                default:
                    System.out.println("Opcion invalida. Intente de nuevo.");
            }
        }while (opcion != 3);

        sc.close();
    }
}