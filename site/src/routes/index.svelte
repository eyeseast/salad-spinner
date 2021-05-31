<script context="module">
	import { assets } from "$app/paths";

	export async function load({ page, fetch, session, context }) {
		const res = await fetch(`${assets}/ingredients.json`);
		const { types, ...ingredients } = await res.json();

		return { props: { types, ingredients } };
	}
</script>

<script>
	import { onMount } from "svelte";
	import Layer from "$lib/Layer.svelte";
	import { layers } from "$lib/stores.js";

	export let ingredients = {};
	export let types = {};

	onMount(() => {
		layers.restore();
	});
</script>

<svelte:head>
	<title>Salad Spinner</title>
</svelte:head>

<h1>Salad spinner</h1>

<h2>Add something</h2>
<ul class="types">
	{#each Object.entries(types) as [id, type]}
		<li><button on:click={e => layers.add(id)}>{type.name}</button></li>
	{/each}
</ul>

<form class="layers">
	{#each $layers as layer, index (layer)}
		<Layer
			id={layer.type}
			name={types[layer.type].name}
			ingredients={ingredients[layer.type]}
			{index}
		/>
	{/each}

	<div class="submit">
		<input type="submit" value="Save this salad" />
	</div>
</form>
