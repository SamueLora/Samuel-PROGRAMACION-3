/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.vectoress;

/**
 *
 * @author samue
 */
import java.util.*;

public class Vectoress {

    public static void main(String[] args) {
        // Declarar una lista vacía
        ArrayList<Integer> lista_vacia = new ArrayList<>();
        System.out.println(lista_vacia);
        
        // Declarar una lista con más de 5 elementos
        ArrayList<Integer> lista_mas_cinco = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7));
        System.out.println(lista_mas_cinco);
        // Encuentra la longitud de tu lista
        int longitud_lista = lista_mas_cinco.size();
        System.out.println(longitud_lista);
        // Obtener el primer elemento, el elemento central y el último elemento de la lista
        int primer_elemento = lista_mas_cinco.get(0);
        System.out.println(primer_elemento);
        int elemento_central = lista_mas_cinco.get(lista_mas_cinco.size() / 2);
        System.out.println(elemento_central);
        int ultimo_elemento = lista_mas_cinco.get(lista_mas_cinco.size() - 1);
        System.out.println(ultimo_elemento);

        // Declarar una lista llamada tipos_datos_mezclados
        Object tu_edad = 19;
        double tu_altura = 1.82;
        ArrayList<Object> tipos_datos_mezclados = new ArrayList<>(Arrays.asList("Samuel", tu_edad, tu_altura, "Soltero", "Micasa barrio: Mibarrio"));
        System.out.println(tipos_datos_mezclados);
        // Declarar una variable de lista llamada it_companies
        ArrayList<String> it_companies = new ArrayList<>(Arrays.asList("Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"));
        System.out.println(it_companies);
        // Añadir una empresa de TI a it_companies utilizando los métodos de inserción
        it_companies.add("Yasu Piste");
        System.out.println(it_companies);
        // Comprobar si una determinada empresa existe en la lista it_companies
        boolean empresa_existente = it_companies.contains("Google");
        System.out.println(empresa_existente);
        // Ordenar la lista con el método sort()
        Collections.sort(it_companies);
        System.out.println(it_companies);
        // Invertir la lista en orden descendente utilizando el método reverse()
        Collections.reverse(it_companies);
        System.out.println(it_companies);
        // Eliminar la primera empresa informática de la lista
        String primer_empresa = it_companies.remove(0);
        System.out.println(it_companies);
        // Eliminar todas las empresas de TI de la lista
        it_companies.clear();
        System.out.println(it_companies);
    }
}