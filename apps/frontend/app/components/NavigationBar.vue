<style scoped>
.active-link {
  color: white;
  text-shadow: 0 0 12px rgba(99,102,241,0.6);
}
</style>

<template>
  <nav class="w-full">
    <div class="px-4 py-4 fixed w-full z-50 glass rounded-b-lg">
      <div
        class="flex items-center justify-between"
      >

        <!-- Brand -->
        <NuxtLink
          to="/"
          class="flex items-center gap-3 text-lg font-semibold hover:scale-105 transition-all"
        >
          <span class="gradient-text">
            LLM Studio
          </span>
        </NuxtLink>

        <!-- Links -->
        <div
			class="hidden md:flex items-center gap-10
					space-x-20
					text-sm font-medium
					text-(--text-soft)
					group"
		>
          <NuxtLink
			v-for="link in links"
			:key="link.to"
			:to="link.to"
			class="
				transition-all duration-300 ease-out

				group-hover:opacity-60
				group-hover:scale-[0.96]

				hover:opacity-100!
				hover:scale-105!
				hover:text-white

				active:scale-95
			"
			active-class="active-link"
			>
			{{ link.label }}
		</NuxtLink>

        </div>

        <!-- CTA -->
        <client-only>
			<appkit-button/>
		</client-only>


      </div>
    </div>
  </nav>
</template>

<script lang="ts" setup>
	import "~/composables/useWallet"
	interface NavLink {
		to: string
		label: string
	}

	const links: NavLink[] = [
		{ to: '/', label: 'Home' },
		{ to: '/build', label: 'Build' },
		{ to: '/docs', label: 'Docs' },
		{ to: '/about', label: 'About' },
	]
</script>
