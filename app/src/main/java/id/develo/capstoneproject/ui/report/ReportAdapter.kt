package id.develo.capstoneproject.ui.report

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import id.develo.capstoneproject.data.local.entity.ReportEntity
import id.develo.capstoneproject.databinding.ItemReportBinding

class ReportAdapter(private val listReports: ArrayList<ReportEntity>) :
    RecyclerView.Adapter<ReportAdapter.ReportViewHolder>() {

    inner class ReportViewHolder(private val binding: ItemReportBinding) :
        RecyclerView.ViewHolder(binding.root) {
            fun bind(report: ReportEntity) {
                with(binding) {
                    tvStreet.text = report.latitude.toString()
                    tvCategory.text = report.holeType
                    Glide.with(itemView.context)
                        .load("https://storage.googleapis.com/pothole-detection1/" + report.urlImg)
                        .into(imgUser)
                }
            }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ReportViewHolder {
        val binding =
            ItemReportBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return ReportViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ReportViewHolder, position: Int) {
        holder.bind(listReports[position])
    }

    override fun getItemCount(): Int = listReports.size
}