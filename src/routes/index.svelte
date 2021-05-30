<script context="module">
	import { assets } from '$app/paths';
	import Layer from '$lib/Layer.svelte';

	export async function load({ page, fetch, session, context }) {
		const res = await fetch(`${assets}/ingredients.json`);
		const { types, ...ingredients } = await res.json();

		return { props: { types, ingredients } };
	}
</script>

<script>
	export let ingredients = {};
	export let types = {};

	let layers = [];

	function add(type) {
		layers = [...layers, { type, ingredient: null }];
	}
</script>

<svelte:head>
	<title>Salad Spinner</title>
</svelte:head>

<h1>Salad spinner</h1>

<ul class="types">
	{#each Object.entries(types) as [id, type]}
		<li><button on:click={e => add(id)}>{type.name}</button></li>
	{/each}
</ul>

<div class="layers">
	<!--
	{#each Object.entries(ingredients) as [layer, ingredients], index}
		<Layer id={layer} name={types[layer].name} {ingredients} {index} />
	{/each}
	-->
	{#each layers as layer, index}
		<Layer
			id={layer.type}
			name={types[layer.type].name}
			ingredients={ingredients[layer.type]}
			{index}
		/>
	{/each}
</div>
