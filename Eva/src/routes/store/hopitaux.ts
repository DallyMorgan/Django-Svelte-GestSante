// hopitaux.ts

import { writable } from 'svelte/store';
import axios from 'axios';
//import {Hopital} from './hopit'
import type { Hopital } from './hopit';
import type { Patient } from './hopit';






// Création d'un store nommé 'hopitaux' avec une valeur initiale vide
export const hopitaux = writable<Hopital[]>([]);

export const Patients = writable<Patient[]>([]);

// Fonction pour récupérer les données des hôpitaux depuis l'API
export const fetchHopitaux = async () => {
    try {
        // Remplacer l'URL de l'API par l'URL réelle de votre API
        const response = await axios.get<Hopital[]>('http://127.0.0.1:8000/api/hopitaux/');
        const data = response.data;
        // Mettre à jour le store 'hopitaux' avec les données transformées
        hopitaux.set(data);
    } catch (error) {
        console.error('Erreur lors de la récupération des hôpitaux:', error);
    }
};
export type { Hopital };





// Fonction pour envoyer les données du formulaire
export const envoyerPatient = async (patient: Patient) => {
    try {
        // Remplacez l'URL par l'adresse réelle de votre API
        const url = 'http://127.0.0.1:8000/api/Patients/';

        // Envoi de la requête POST avec Axios
        const response = await axios.post<Patient>(url, patient);

        // Gérez la réponse (par exemple, affichez-la dans la console)
        console.log('Réponse du serveur :', response.data);
    } catch (error) {
        // Gérez les erreurs (par exemple, affichez-les dans la console)
        console.error('Erreur lors de l\'envoi :', error);
    }
};

export type { Patient };