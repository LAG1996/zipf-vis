<template>
	<article>
		{{text}}
	</article>
</template>

<script>
	export default {
		name: 'colored-doc',
		props: {
			text: '',
		},
		created: function() {
			console.log(this);
		}
	};
</script>

<style>
</style>
