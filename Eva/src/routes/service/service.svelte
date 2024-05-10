<script lang="ts">
	import type { Patient } from './../store/hopit';
	import { envoyerPatient } from './../store/hopitaux';
	import { onMount } from 'svelte';
	import { hopitaux, fetchHopitaux} from './../store/hopitaux';
	import { toast } from '@zerodevx/svelte-toast';
	//import  Patient from './../store/hopit';
	
	let selectedHopital = '';
	let nom = '';
	let tel = '';
	let email = '';
	let service = 0;
	let message = '';

	onMount(async () => {
		await fetchHopitaux();
		console.log(hopitaux)
	});

	$: filteredHopitaux = selectedHopital
		? $hopitaux.filter((hopital) => hopital.nom === selectedHopital)
		: $hopitaux;

    // Fonction pour soumettre le formulaire
    const SubForm = async (event: SubmitEvent) => {
        event.preventDefault(); // Empêche le comportement par défaut du formulaire
		
		// Création d'un objet patient avec les données du formulaire
		let patient: Patient = {nom: nom,tel: tel,email: email,service: service,message: message};

		try {
			// Envoyez les données du patient à votre API
			await envoyerPatient(patient);
			
			// Réinitialisez les champs du formulaire si nécessaire
			nom = "";email = "";tel = "";service = 0;message = "";
		} catch (error) {
			console.error("Erreur lors de l'envoi du formulaire :", error);
		}
	}
</script>


<!-- Service Start -->

<div class="container-fluid container-service py-5">
	<div class="container pt-5">
		<div class="text-center mx-auto wow fadeInUp" data-wow-delay="0.1s" style="max-width: 600px;">
			<h1 class="display-6 mb-3">Service Laboratoire fiable et de haute qualité</h1>
			<select bind:value={selectedHopital} class="form-control my-3">
				<option value="">Sélectionnez un hopital</option>
				{#each $hopitaux as hopital (hopital.id)}
					<option value={hopital.nom}>{hopital.nom}</option>
				{/each}
			</select>
		</div>
		
		<div class="row g-4">
			{#if filteredHopitaux.length > 0}
				{#each filteredHopitaux as hopital}
					{#each hopital.services as service}
						<div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.7s">
							<div class="service-item">
								<div class="icon-box-primary mb-4">
									<i class="bi bi-file-medical text-dark"></i>
								</div>
								<h5 class="mb-3">{service.nom}</h5>
								{#each service.appareils as appareil}
									<p class="mb-4">- {appareil.nom}</p>
								{/each}

								<a class="btn btn-light px-3" href="/">
									{#if service.en_operation}
										Indisponible<i class="bi bi-chevron-double-right ms-1"></i>
									{:else}
										Disponible<i class="bi bi-chevron-double-right ms-1"></i>
									{/if}
								</a>
							</div>
						</div>
					{/each}
				{/each}
			{:else}
				<p>Pas d'hôpitaux</p>
			{/if}
		</div>
			
	</div>
</div>

<!-- Service End 

<!-- Team Start -->

<div class="container-fluid container-team py-5">
	<div class="container pb-5">
		<div class="row g-4">
			{#each filteredHopitaux as hopital}
				{#each hopital.services as service}
					{#each service.medecins as medecin}
						<div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.3s">
							<div class="team-item">
								<div class="position-relative overflow-hidden">
									<img class="img-fluid w-100" src={medecin.photo} alt={medecin.nom} />
									<div class="team-social">
									<p class="btn btn-square text-black mx-1"> Tel: {medecin.tel}</p>
									</div>
								</div>
								<div class="text-center p-4">
									<h5 class="mb-1">{medecin.nom}</h5>
									<span>{medecin.titre}</span>
								</div>
							</div>
						</div>
					{/each}
				{/each}
			{/each}
		</div>
	</div>
</div>
<!-- Team End -->




 <!-- Appoinment Start -->
 <div class="container-fluid py-5">
	<div class="container">
		<div class="row g-5">
			<div class="col-lg-6 wow fadeInUp" data-wow-delay="0.1s">
				<h1 class="display-6 mb-4">Nous veillons a ce que vous obtenez toujours le meilleur resultat</h1>
				<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tellus augue, iaculis id elit eget, ultrices pulvinar tortor. Quisque vel lorem porttitor, malesuada arcu quis, fringilla risus. Pellentesque eu consequat augue.</p>
				<p class="mb-4">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tellus augue, iaculis id elit eget, ultrices pulvinar tortor.</p>
				<div class="d-flex align-items-start wow fadeIn" data-wow-delay="0.3s">
					<div class="icon-box-primary">
						<i class="bi bi-geo-alt text-dark fs-1"></i>
					</div>
					<div class="ms-3">
						<h5>Address</h5>
						<span>123 Street, Rabbat, Maroc</span>
					</div>
				</div>
				<hr>
				<div class="d-flex align-items-start wow fadeIn" data-wow-delay="0.4s">
					<div class="icon-box-primary">
						<i class="bi bi-clock text-dark fs-1"></i>
					</div>
					<div class="ms-3">
						<h5>Horraires</h5>
						<span>Lun-Sa 09h-17h, Dim fermé</span>
					</div>
				</div>
			</div>
			<div class="col-lg-6 wow fadeInUp" data-wow-delay="0.5s">
				<h2 class="mb-4">Prendre Rendez-vous</h2>
				<form on:submit={SubForm} >
				<div class="row g-3">
					<div class="col-sm-6">
						<div class="form-floating">
							<input type="text" class="form-control" required id="name" placeholder="Your Name" bind:value="{nom}">
							<label for="name">Votre nom</label>
						</div>
					</div>
					<div class="col-sm-6">
						<div class="form-floating">
							<input type="email" class="form-control" required id="mail" placeholder="Your Email" bind:value="{email}">
							<label for="mail">Votre Email</label>
						</div>
					</div>
					<div class="col-sm-6">
						<div class="form-floating">
							<input type="text" class="form-control"  required id="mobile" placeholder="Your Mobile" bind:value="{tel}">
							<label for="mobile">Numero telephone</label>
						</div>
					</div>
					<div class="col-sm-6">
						<div class="form-floating">
							<select class="form-select" required id="service" bind:value="{service}">
								{#each filteredHopitaux as hopital}
									{#each hopital.services as service}
										<option value={service.id} selected>{service.nom}</option>
									{/each}    
								{/each}
							</select>
							
							<label for="service">Choisir un Service</label>
						</div>
					</div>
					<div class="col-12">
						<div class="form-floating">
							<textarea class="form-control" bind:value="{message}" placeholder="Leave a message here" id="message"
								style="height: 130px"></textarea>
							<label for="message">Message</label>
						</div>
					</div>
					<div class="col-12 text-center">
						<button class="btn btn-primary w-100 py-3" type="submit">Soumettre</button>
					</div>
				</div>
			</form>
			</div>
		</div>
	</div>
</div>
<!-- Appoinment Start -->