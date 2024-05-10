// Interface pour représenter un médecin
interface Medecin {
    id: number;
    nom: string;
    titre: string;
    tel: string;
    photo: string;
}

// Interface pour représenter un appareil
interface Appareil {
    id: number;
    nom: string;
}


 export interface Patient {
    nom: string;
    tel: string;
    email: string;
    service: number;
    message: string;
}

// Interface pour représenter un service
interface Service {
    id: number;
    nom: string;
    en_operation: boolean;
    medecins: Medecin[];
    appareils: Appareil[];
}

// Interface pour représenter un hôpital
export interface Hopital {
    id: number;
    nom: string;
    services: Service[];
}
