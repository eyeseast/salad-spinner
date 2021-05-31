<script>
	import { onMount } from "svelte";
	import { layers } from "$lib/stores.js";

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
	<label
		>{name}
		<select name={id}>
			<option value="" />
			{#each ingredients as ingredient}
				<option selected={ingredient === current} value={ingredient.name}
					>{ingredient.name}</option
				>
			{/each}
		</select>
	</label>
	<button on:click={set}>Shuffle</button>
	<button on:click={layers.remove(index)}>Remove</button>
</div>
