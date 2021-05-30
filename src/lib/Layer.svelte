<script>
	import { onMount } from 'svelte';
	export let name;
	export let id;
	export let index;
	export let ingredients = [];

	let current;

	export function choose() {
		current = ingredients[Math.floor(Math.random() * ingredients.length)];
	}

	onMount(() => {
		choose();
	});
</script>

<div class="layer" {id} data-index={index}>
	<h2>{name}</h2>
	<ul class="ingredients">
		{#each ingredients as ingredient}
			<li class:current={ingredient === current}>{ingredient.name}</li>
		{/each}
	</ul>
	<button on:click={choose}>Choose</button>
</div>

<style>
	.current {
		font-weight: bold;
	}
</style>
