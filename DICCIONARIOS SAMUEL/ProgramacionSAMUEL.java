/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package programacionsamuel;

/**
 *
 * @author Sala de Sistemas
 */
import java.util.*;

public class ProgramacionSAMUEL {
    
    public static void main(String[] args) {
        // #1
        System.out.println("#1");
        HashMap<String, String> perro = new HashMap<>();
        System.out.println(perro);
        System.out.println();

        // #2
        System.out.println("#2");
        perro.put("nombre", "Roberto");
        perro.put("color", "Marrón");
        perro.put("raza", "Rottweiler");
        perro.put("patas", "4");
        perro.put("edad", "10 meses");
        System.out.println(perro);
        System.out.println();

        // #3
        System.out.println("#3");
        HashMap<String, Object> estudiante = new HashMap<>();
        estudiante.put("nombre", "Samuel");
        estudiante.put("apellido", "Lora");
        estudiante.put("sexo", "Masculino");
        estudiante.put("edad", "19");
        estudiante.put("estado_civil", "Soltero");
        List<String> habilidades = new ArrayList<>();
        habilidades.add("Programador");
        estudiante.put("habilidades", habilidades);
        estudiante.put("pais", "Colombia");
        estudiante.put("ciudad", "Cartagena");
        estudiante.put("direccion", "Mi casa, cra Micasa123");
        System.out.println(estudiante);
        System.out.println();

        // #4
        System.out.println("#4");
        System.out.println(estudiante.size());
        System.out.println();

        // #5
        System.out.println("#5");
        System.out.println(estudiante.get("habilidades"));
        System.out.println(estudiante.get("habilidades").getClass());
        System.out.println();

        // #6
        System.out.println("#6");
        List<String> habilidadesEstudiante = (List<String>) estudiante.get("habilidades");
        habilidadesEstudiante.add("Bilingue");
        System.out.println(estudiante);
        System.out.println();

        // #7
        System.out.println("#7");
        Set<String> keys = estudiante.keySet();
        System.out.println(keys);
        System.out.println();

        // #8
        System.out.println("#8");
        Collection<Object> values = estudiante.values();
        System.out.println(values);
        System.out.println();

        // #9
        System.out.println("#9");
        Set<Map.Entry<String, Object>> entries = estudiante.entrySet();
        System.out.println(entries);
        System.out.println();

        // #10
        System.out.println("#10");
        estudiante.remove("direccion");
        System.out.println(estudiante);
        System.out.println();

        // #11
        System.out.println("#11");
        estudiante = null;
        System.out.println();
    }
}