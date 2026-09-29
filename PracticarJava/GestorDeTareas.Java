import java.util.Scanner;

public class GestorDeTareas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int totalPrioridad = 0;

        System.out.println("=== Gestor de Tareas. ===");
        System.out.println("1. Agregar tarea.");
        System.out.println("2. Ver tareas. (Pendientes)");
        System.out.println("3. Salir.");

        System.out.print("Selecciona una opcion: ");
        int opcion = sc.nextInt();
        sc.nextLine(); // Limpiar

        // Validamos que este entre 1 y 3
        if (opcion >= 1 && opcion <=3) {
            if (opcion == 1) {
                System.out.print("Nombre de la tarea: ");
                String nombreTarea =sc.nextLine();

                System.out.print("Prioridad (1 al 5): ");
                int prioridad = sc.nextInt();

                // Validacion basica con operador logico.
                boolean esValida = prioridad >= 1 && prioridad <= 5;
                System.out.println("Prioridad valida? " + esValida);

                // Operacion aritmetica: sima de prioridades
                totalPrioridad += prioridad;

                System.out.println("Tarea agregada: " + nombreTarea + "(Prioridad " + prioridad + ")");
                System.out.println("Suma total de prioridades: " + totalPrioridad);
            } else if (opcion == 2) {
                System.out.println("Funcion 'ver tareas' aun no implementada.");
            } else {
                System.out.println("Hasta luego!");
            }
        } else {
            System.out.println("Opcion invalida.");
        }

        sc.close();
    }
}