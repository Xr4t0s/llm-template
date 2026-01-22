<template>
  <footer class="w-full mt-24">
    <div
      class="
        mx-auto
        max-w-7xl
        px-6
        py-6
        glass
        rounded-2xl
      "
    >
      <div
        class="
          flex
          flex-col
          sm:flex-row
          items-center
          justify-between
          gap-6
          text-sm
          text-(--text-soft)
        "
      >
        <!-- Social icons -->
        <div class="flex items-center gap-5">
          <a
            v-for="item in socials"
            :key="item.name"
            :href="item.href"
            target="_blank"
            rel="noopener noreferrer"
            class="
              transition-all
              hover:text-white
              hover:scale-110
              active:scale-95
            "
            :aria-label="item.name"
          >
            <Icon
              :icon="item.icon"
              class="w-5 h-5"
            />
          </a>
        </div>

        <!-- Meta -->
        <div class="text-xs text-(--text-soft)">
          © {{ year }} LLM Studio
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { Icon } from '@iconify/vue'

const year = new Date().getFullYear()

const socials = [
  {
    name: 'GitHub',
    href: 'https://github.com/your-org',
    icon: 'mdi:github',
  },
  {
    name: 'Twitter',
    href: 'https://twitter.com/your-handle',
    icon: 'mdi:twitter',
  },
  {
    name: 'Discord',
    href: 'https://discord.gg/your-invite',
    icon: 'mdi:discord',
  },
]
</script>
