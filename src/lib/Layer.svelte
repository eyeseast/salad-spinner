<script>
	import { onMount } from 'svelte';
	import { layers } from '$lib/stores.js';

	export let name;
	export let id;
	export let index;
	export let ingredients = [];

	$: current = $layers[index].ingredient;

	export function choose() {
		return ingredients[Math.floor(Math.random() * ingredients.length)];
	}

	function set() {
		$layers[index].ingredient = choose();
	}

	onMount(() => {
		set();
	});
</script>

<div class="layer" {id} data-index={index}>
	<h2>{name}</h2>
	<ul class="ingredients">
		{#each ingredients as ingredient}
			<li class:current={ingredient === current}>{ingredient.name}</li>
		{/each}
	</ul>
	<button on:click={set}>Choose</button>
	<button on:click={layers.remove(index)}>Remove</button>
</div>

<style>
	.current {
		font-weight: bold;
	}
</style>
